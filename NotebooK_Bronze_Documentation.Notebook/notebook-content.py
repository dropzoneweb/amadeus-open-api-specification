# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
Here’s a structured summary of your **OAuth token retrieval workflow** for easy documentation. You can copy-paste this into your **Bronze metadata table** or **OneLake storage** for future reference.

---

# **Amadeus API Authentication & Token Retrieval Workflow**
## **Purpose**
This workflow enables **OAuth 2.0 authentication** for securely retrieving and using access tokens in a **Microsoft Fabric Data Pipeline**.

## **Pipeline Components**
### **1. Web Activity: Token Retrieval**
- **Connection**: HTTP Linked Service (`https://test.api.amadeus.com`)
- **Relative URL**: `/v1/security/oauth2/token`
- **Method**: `POST`
- **Headers**:  
  ```
  Content-Type: application/x-www-form-urlencoded
  Accept: application/json
  ```
- **Body (URL-encoded)**:  
  ```
  grant_type=client_credentials&client_id=<your_client_id>&client_secret=<your_client_secret>
  ```

### **2. Set Variable Activity: Store OAuth Token**
- **Variable Name**: `OAuthToken`
- **Expression**:  
  ```
  @activity('WebActivityName').output.access_token
  ```
- **Purpose**: Captures the returned access token for reuse in subsequent API calls.

### **3. Web Activity: API Data Retrieval**
- **Relative URL**: Set the API endpoint for fetching data.
- **Method**: `GET`
- **Headers**:
  ```
  Authorization: Bearer @{variables('OAuthToken')}
  Accept: application/json
  ```
- **Purpose**: Calls the API using the stored token.

### **4. Debug & Logging Strategy**
- Enable **debug mode** to inspect execution logs.
- Add a temporary **Set Variable** activity with:
  ```
  @string(activity('WebActivityName').output)
  ```
  to verify API response structure before extracting the token.

---

## **Recommendations for Storage in Bronze Layer**
- **Metadata Table (Structured Storage)**:
  - Store key configuration details in a Bronze-layer table:
    ```
    | ProcessName   | Description                | LastUpdated | KeyParameters  |
    |--------------|--------------------------|------------|---------------|
    | Amadeus OAuth | API authentication setup | 2025-06-11  | Client ID, Token Expiry |
    ```
  
- **OneLake Documentation Folder (Unstructured Storage)**:
  - Maintain a **Markdown (.md) or Text (.txt) file** in OneLake under:
    ```
    /BronzeLayer/Docs/API_Auth.md
    ```
  - Include steps for troubleshooting, retries, and future optimizations.

---

This should make it easy to retrieve, reference, and modify pipeline authentication details in the future. Would you like to add **token refresh automation** or **retry logic** to make sure this setup remains reliable? 🚀🔧



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# {
#   "currencyCode": "USD",
#   "originDestinations": [
#     {
#       "id": "1",
#       "originLocationCode": "LAX",
#       "destinationLocationCode": "BOG",
#       "departureDateTimeRange": {
#         "date": "2025-07-01",
#         "time": "10:00:00"
#       }
#     }
#   ],
#   "travelers": [
#     {
#       "id": "1",
#       "travelerType": "ADULT"
#     }
#   ],
#   "sources": [
#     "GDS"
#   ],
#   "searchCriteria": {
#     "maxFlightOffers": 5,
#     "flightFilters": {
#       "cabinRestrictions": [
#         {
#           "cabin": "BUSINESS",
#           "coverage": "MOST_SEGMENTS",
#           "originDestinationIds": [
#             "1"
#           ]
#         }
#       ]
#     }
#   }
# }

# MARKDOWN ********************

# Here are **AI Agent-related skills** tailored to each of the Microsoft technologies you specialize in. These skills range from **entry-level to intermediate**, ensuring they align with your growing expertise in AI-driven automation.
# 
# ### **Microsoft Entra ID (IAM & Compliance)**
# 1. **AI-Driven Access Review Automation** – Implement identity governance workflows using AI-powered Entra reviews.
# 2. **Adaptive Authentication Policies with AI** – Configure conditional access policies leveraging AI-based risk assessment.
# 3. **Automated Role-Based Access Control (RBAC) Recommendations** – Use AI to optimize role assignments based on behavioral analysis.
# 
# ### **Microsoft Purview (Data Governance & Monitoring)**
# 1. **AI-Powered Data Classification & Sensitivity Labeling** – Configure automatic classification using AI models.
# 2. **AI-Assisted Compliance Monitoring** – Leverage AI-driven alerts and anomaly detection for compliance enforcement.
# 3. **Natural Language Querying for Data Discovery** – Utilize AI-enabled search for locating sensitive information across cloud storage.
# 
# ### **Microsoft Fabric (Data Engineering & AI Integration)**
# 1. **AI-Driven Data Pipeline Optimization** – Implement performance monitoring and cost-efficient workflows using AI.
# 2. **AutoML Model Deployment in Fabric Notebooks** – Build and integrate predictive models into Fabric workflows.
# 3. **AI-Based Query Performance Enhancement** – Use intelligent caching and optimization techniques to streamline Fabric SQL queries.
# 
# ### **Power BI (Analytics & AI Integration)**
# 1. **AI-Driven Insights with Smart Narrative** – Generate automated summaries of dashboards using AI-powered analysis.
# 2. **Automated Anomaly Detection in Reports** – Enable AI-based data trend detection to highlight unusual metrics.
# 3. **Natural Language Q&A for Interactive Data Exploration** – Use AI-enhanced querying for dynamic, real-time insights.
# 
# ### **SharePoint Online (Content & Knowledge Management)**
# 1. **AI-Powered Content Tagging & Metadata Extraction** – Automate classification of documents using machine learning.
# 2. **Intelligent Search & Semantic Retrieval** – Enhance enterprise search with AI-based document relevance ranking.
# 3. **AI-Based Workflow Automation in Lists & Libraries** – Utilize AI to predict and automate common task workflows.
# 
# ### **Copilot Studio (Conversational AI & Workflow Automation)**
# 1. **Prompt Engineering for AI Agents** – Design optimized prompts for Copilot's natural language processing.
# 2. **Workflow Automation using AI Bots** – Build conversational flows that trigger automated business processes.
# 3. **AI-Powered Sentiment & Intent Recognition** – Implement sentiment analysis for improved chatbot responses.
# 
# These skills will help position you as an **IAM & Compliance expert integrating AI-driven automation**, while also showcasing **your expanding expertise in RAG and AI-powered optimization**. Would you like help structuring your resume to highlight these AI agent skills effectively? 🚀🔧
# 


# MARKDOWN ********************

# Here’s a **complete list** of the **Amadeus Self-Service APIs**, including **Flights sub-categories** and their **API endpoint URLs**:
# 
# ### **Flights APIs**
# #### **Flight Booking**
# - **Flight Offers Search** – Search flights between cities.  
#   **Endpoint:** [`/v2/shopping/flight-offers`](^4^)  
# - **Flight Offers Price** – Confirm flight availability and pricing.  
#   **Endpoint:** [`/v2/shopping/flight-offers/pricing`](^4^)  
# - **Flight Create Orders** – Book flights and get reservation details.  
#   **Endpoint:** [`/v1/booking/flight-orders`](^4^)  
# - **Flight Order Management** – Manage flight reservations.  
#   **Endpoint:** [`/v1/booking/flight-orders/{orderId}`](^4^)  
# 
# #### **Flight Inspiration**
# - **Flight Inspiration Search** – Discover destinations based on price.  
#   **Endpoint:** [`/v1/shopping/flight-destinations`](^4^)  
# - **Flight Cheapest Date Search** – Find the cheapest travel dates.  
#   **Endpoint:** [`/v1/shopping/flight-dates`](^4^)  
# - **Flight Availabilities Search** – Check flight availability.  
#   **Endpoint:** [`/v1/shopping/availability`](^4^)  
# - **Travel Recommendations** – Get personalized travel suggestions.  
#   **Endpoint:** [`/v1/shopping/recommendations`](^4^)  
# 
# #### **Flight Schedule**
# - **On-Demand Flight Status** – Retrieve real-time flight status.  
#   **Endpoint:** [`/v2/schedule/flights`](^4^)  
# - **Flight Delay Prediction** – Predict flight delays.  
#   **Endpoint:** [`/v1/travel/predictions/flight-delay`](^4^)  
# 
# #### **Airport APIs**
# - **Airport & City Search** – Search for airport and city details.  
#   **Endpoint:** [`/v1/reference-data/locations`](^4^)  
# - **Airport Nearest Relevant** – Find the nearest relevant airport.  
#   **Endpoint:** [`/v1/reference-data/locations/airports`](^4^)  
# - **Airport Routes API** – Get airport route details.  
#   **Endpoint:** [`/v1/airport/routes`](^4^)  
# - **Airport On-Time Performance** – Analyze airport punctuality.  
#   **Endpoint:** [`/v1/airport/on-time-performance`](^4^)  
# 
# ### **Hotels APIs**
# - **Hotel Search** – Find hotels with pricing and availability.  
#   **Endpoint:** [`/v2/shopping/hotel-offers`](^4^)  
# - **Hotel Ratings** – Get customer feedback on hotels.  
#   **Endpoint:** [`/v2/shopping/hotel-offers/{hotelId}/ratings`](^4^)  
# - **Hotel Booking** – Book hotels directly.  
#   **Endpoint:** [`/v1/booking/hotel-bookings`](^4^)  
# 
# ### **Cars and Transfers APIs**
# - **Transfer Search** – Find transfer providers.  
#   **Endpoint:** [`/v1/shopping/transfer-offers`](^4^)  
# - **Transfer Booking** – Book transfer services.  
#   **Endpoint:** [`/v1/booking/transfer-orders`](^4^)  
# 
# ### **Destination Experiences APIs**
# - **Points of Interest** – Discover local attractions.  
#   **Endpoint:** [`/v1/reference-data/locations/pois`](^4^)  
# - **Tours and Activities** – Find experiences and activities.  
#   **Endpoint:** [`/v1/shopping/activities`](^4^)  
# 
# ### **Market Insights APIs**
# - **Flight Most Traveled Destinations** – Explore top travel destinations.  
#   **Endpoint:** [`/v1/travel/analytics/most-traveled`](^4^)  
# - **Flight Most Booked Destinations** – View booking trends.  
#   **Endpoint:** [`/v1/travel/analytics/most-booked`](^4^)  
# - **Flight Busiest Traveling Period** – Analyze peak travel times.  
#   **Endpoint:** [`/v1/travel/analytics/busiest-periods`](^4^)  
# 
# ### **Itinerary Management APIs**
# - **Trip Purpose Prediction** – Predict trip purposes.  
#   **Endpoint:** [`/v1/travel/predictions/trip-purpose`](^4^)  
# 
# For **full API documentation**, visit the official [Amadeus Self-Service API Docs](https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/resources/flights/). Let me know if you need more details!

