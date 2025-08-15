
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/nyc_311_service_requests.csv")

# Convert 'Created Date' and 'Closed Date' to datetime objects
df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M:%S %p')
df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

# Calculate resolution time
df['Resolution Time'] = (df['Closed Date'] - df['Created Date']).dt.total_seconds() / 3600  # in hours

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

print("\nDataset Head:")
print(df.head())

print("\nDataset Description:")
print(df.describe())

# Top 10 Complaint Types
top_complaint_types = df['Complaint Type'].value_counts().head(10)
print("\nTop 10 Complaint Types:")
print(top_complaint_types)

plt.figure(figsize=(12, 7))
sns.barplot(x=top_complaint_types.values, y=top_complaint_types.index, palette='viridis')
plt.title('Top 10 Complaint Types in NYC 311 Service Requests')
plt.xlabel('Number of Requests')
plt.ylabel('Complaint Type')
plt.tight_layout()
plt.savefig('/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/top_complaint_types.png')
print("Top 10 Complaint Types plot saved as top_complaint_types.png")

# Complaint Types by Borough
complaints_by_borough = df.groupby('Borough')['Complaint Type'].value_counts().unstack(fill_value=0)
print("\nComplaint Types by Borough:")
print(complaints_by_borough.head())

# Plotting top 5 complaint types by borough
plt.figure(figsize=(15, 8))
complaints_by_borough.iloc[:, :5].plot(kind='bar', stacked=True, colormap='Paired')
plt.title('Top 5 Complaint Types by Borough')
plt.xlabel('Borough')
plt.ylabel('Number of Requests')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/complaints_by_borough.png')
print("Complaint Types by Borough plot saved as complaints_by_borough.png")

# Average Resolution Time by Complaint Type (for closed requests)
avg_resolution_time = df[df['Status'] == 'Closed'].groupby('Complaint Type')['Resolution Time'].mean().sort_values(ascending=False).head(10)
print("\nAverage Resolution Time by Complaint Type (Top 10):")
print(avg_resolution_time)

plt.figure(figsize=(12, 7))
sns.barplot(x=avg_resolution_time.values, y=avg_resolution_time.index, palette='magma')
plt.title('Average Resolution Time by Complaint Type (Top 10)')
plt.xlabel('Average Resolution Time (Hours)')
plt.ylabel('Complaint Type')
plt.tight_layout()
plt.savefig('/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/avg_resolution_time.png')
print("Average Resolution Time plot saved as avg_resolution_time.png")

# Save some analysis results to CSV
top_complaint_types.to_csv("/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/top_complaint_types.csv")
complaints_by_borough.to_csv("/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/complaints_by_borough.csv")
avg_resolution_time.to_csv("/home/ubuntu/data_portfolio/NYC_311_Service_Request_Analysis/avg_resolution_time.csv")

print("\nAnalysis complete. Results saved to CSV files and plots.")


