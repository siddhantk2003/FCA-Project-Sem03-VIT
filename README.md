# FCA-Project-Sem03-VIT
Project on Web Scrapping for Course - "Financial &amp; Cost Accounting" in Semester-03 at VITV

(I) Overview of 10-K Reports and Financial Metrics
The 10-K reports are comprehensive annual filings that publicly traded companies submit to the U.S. Securities and Exchange Commission (SEC). These reports provide a detailed overview of a company’s financial performance, operations, and risks over the past fiscal year. 
The consolidated financial statements within the 10-K are particularly significant as they present the company’s financial position, profitability, and cash flows in a consolidated format, considering all subsidiaries and business segments.

Key financial metrics that can be extracted from the consolidated financial statements include:
	•	Sales or revenue
	•	Research and development expenses
	•	Profit before tax (EBIT)
	•	Corporate tax provision
	•	Total assets
	•	Plant, property, and equipment (PPE)
	•	Intangible assets and goodwill
	•	Inventories
	•	Executive compensation
	•	Tax haven subsidiaries
	•	Auditor fees
	•	Foreign income
These metrics offer valuable insights into a company’s financial health, efficiency, and potential risks.
Two reliable sources for analysing 10-K reports and financial metrics of a company are  - Investopedia and SEC’s EDGAR database.


(II) Data Scraping Strategy	
The scraping strategy includes the following key steps:

Reading Company Data: The program reads a list of companies from a CSV file (sp500.csv). It assumes each company has relevant data, including its CIK (Central Index Key), which is crucial for querying SEC’s EDGAR system.
Fetching Submissions: For each company, the script calls getSubmissionsByCik() from the edgarpython library to get the list of all submissions made by the company, filtering only for Form 10-K (annual reports).
Downloading Data: For each 10-K form, the URL to the Excel file is retrieved using getXlsxUrl(), and the file is downloaded using the requests library.
Error Handling: The script handles certain errors such as invalid CIKs (via InvalidCIK exception) and missing URLs (via FileNotFoundError).
Progress Tracking: The rich library is used to provide a progress bar for better visualization of scraping progress.

Libraries Used : 
requests:
Used to make HTTP requests for downloading files. This library allows the script to request and retrieve data (e.g., Excel files) from URLs.
Includes setting custom HTTP headers, such as a User-Agent, to mimic a real browser and avoid immediate blocking by anti-scraping measures.
edgarpython:
A custom/third-party library for interacting with the SEC EDGAR API.
It helps in fetching company submissions (with getSubmissionsByCik()) and getting URLs of specific reports (getXlsxUrl()).
rich:
A library that enhances the terminal output by adding a progress bar using track() to visually track the progress of downloading reports for each company.
os:
Used for file and directory operations. This ensures that the necessary output directories are created for storing downloaded files.
csv.reader:
This built-in CSV reader is used to process the input data file (sp500.csv) containing a list of companies and their information.


(III) Data Validation and Cleanup
After scraping the data, it is validated and cleaned to ensure accuracy and consistency. This process involves:
Checking for missing or erroneous data points and handling them appropriately (e.g., filling in missing values, removing outliers).
Verifying the data types and converting them to the correct format (e.g., converting monetary values to numeric format).
Ensuring the CSV file structure is consistent with the specified headers and data organization.
Documenting the validation and cleanup process for future reference.


(IV) Performance Optimisation
To optimize the performance of the Python code, the following techniques can be employed:
Implementing multithreading or asynchronous requests to parallelize the data extraction process and reduce overall run-time.
Utilizing efficient data structures and algorithms to handle large amounts of data efficiently.
Caching or storing intermediate results to avoid redundant computations or network requests.
Continuously monitoring and optimizing the script’s performance based on feedback and profiling results.


(V) Summary and Reflection
Scraping and handling large-scale financial data from 10-K reports presents several challenges, such as navigating complex HTML structures, handling pagination, and ensuring data consistency. However, this process also offers valuable insights and applications in financial analysis and research.
The extracted data can be used to:
Perform comparative analysis across companies and industries
Identify trends and patterns in financial metrics over time
Develop predictive models for financial performance and risk assessment
Support investment decisions and portfolio management
Overall, this assignment has enhanced my understanding of data scraping techniques and their applications in the financial domain. It has also highlighted the importance of data validation, cleanup, and optimization in working with large datasets.

