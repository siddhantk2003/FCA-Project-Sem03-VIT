import os
from csv import reader
from edgarpython.exceptions import InvalidCIK
from edgarpython.secapi import getSubmissionsByCik, getXlsxUrl
from requests import get
from rich.progress import track


def download_file(url, filename):
    """Download a file from the specified URL and save it to the given filename."""
    response = get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
        },
    )
    with open(filename, "wb") as file:
        file.write(response.content)


def create_output_directory(directory):
    """Create an output directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.mkdir(directory)


def process_company(company):
    """Process the submissions for a given company."""
    try:
        submissions = getSubmissionsByCik(company[6])
        selected_submissions = [sub for sub in submissions if sub.form == "10-K"]

        print(f"Found {len(selected_submissions)} 10-K reports for {company[1]}")

        download_urls = []
        missed_count = 0

        for submission in selected_submissions:
            try:
                download_urls.append(getXlsxUrl(company[6], submission.accessionNumber))
            except FileNotFoundError:
                missed_count += 1

        print(f"{len(download_urls)} reports to be downloaded for {company[6]} [missed {missed_count}]")

        total_downloads = len(download_urls)

        for idx, download_url in enumerate(download_urls, start=1):
            filename = f"Output/{company[1]}/{download_url.split('/')[-2]}.xlsx"
            download_file(download_url, filename)
            print(f"Downloaded [{idx}/{total_downloads}]")

    except InvalidCIK:
        print(f"Failed to process {company[1]} due to Invalid CIK.")


def main():
    """Main function to read companies from CSV and initiate downloads."""
    create_output_directory("Output")

    with open("sp500.csv", encoding="utf-8") as file:
        csv_reader = reader(file)
        companies = list(csv_reader)[1:]  # Skip header

    for company in track(companies, description="Processing companies..."):
        company_dir = f"Output/{company[1]}"
        create_output_directory(company_dir)
        process_company(company)


if __name__ == "__main__":
    main()
