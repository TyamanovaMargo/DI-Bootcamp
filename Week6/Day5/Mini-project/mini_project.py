from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd


options = Options()
options.add_argument("--headless")  # Exécuter sans ouvrir une fenêtre de navigateur
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Selenium

driver = webdriver.Chrome(options=options)
url = "https://www.inmotionhosting.com/"
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

plans = soup.find_all("div", class_="imh-rostrum-card")

plan_names = []
discounted_prices = []
renewal_prices = []
features = []


for plan in plans:

    name_tag = plan.find("h3", class_="imh-rostrum-card-title")
    name = name_tag.text.strip() if name_tag else "Not found"

    # Reduced price
    discount_tag = plan.find("div", class_="imh-rostrum-starting-at-price-discounted")
    discount_price = discount_tag.find("span", class_="rostrum-price").text.strip() if discount_tag else "Not found"

    # Renewal price
    renewal_tag = plan.find("div", class_="imh-rostrum-starting-at-price-normal")
    renewal_price = renewal_tag.find("span", class_="rostrum-price").text.strip() if renewal_tag else "Not found"

    # Features
    feature_list = plan.find("ul", class_="imh-rostrum-details-list")
    feature_texts = [li.text.strip() for li in feature_list.find_all("li")] if feature_list else ["Not found"]

    # Add data to lists
    plan_names.append(name)
    discounted_prices.append(discount_price)
    renewal_prices.append(renewal_price)
    features.append(", ".join(feature_texts))


merged_plans = {}

for i in range(len(plan_names)):
    name = plan_names[i]
    promo = discounted_prices[i]
    renewal = renewal_prices[i]
    feature = features[i]

    if name in merged_plans:


        if promo != "Not found":
            merged_plans[name]["Promotional price"] = promo
        if renewal != "Not found":
            merged_plans[name]["Renewal price"] = renewal
        if feature != "Not found":
            merged_plans[name]["Features"].update(feature.split(", "))
    else:
        # Create a new dictionary entry
        merged_plans[name] = {
            "Promotional price": promo,
            "Renewal price": renewal,
            "Features": set(feature.split(", ")) if feature != "Not found" else set(),
        }


final_data = {
    "Plan Name": [],
    "Discounted Price": [],
    "Renewal Price": [],
    "Features": [],
}

# Fill the DataFrame with the merged data
for plan, details in merged_plans.items():
    final_data["Plan Name"].append(plan)
    final_data["Discounted Price"].append(details["Promotional price"])
    final_data["Renewal Price"].append(details["Renewal price"])
    final_data["Features"].append(", ".join(details["Features"]))

# Create the DataFrame
df = pd.DataFrame(final_data)

# Save data to a CSV file
df.to_csv("plans.csv", index=False)

# Show a confirmation message
print("The data was saved in 'plans.csv'.")

# Display the first 5 rows of the DataFrame to check
print(df.head())