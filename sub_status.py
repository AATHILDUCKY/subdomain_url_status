import requests
import concurrent.futures

world_list_name=input("enter your subdomain file name:")

def check_subdomain_status(subdomain, protocol):
    url = f"{protocol}://{subdomain}"
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException:
        return "Failed to connect"

def main():
    with open(f"{world_list_name}", "r") as file:
        subdomains = [line.strip() for line in file]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # You can adjust the number of max_workers as needed for your system
        futures = [executor.submit(check_subdomain_status, subdomain, "http") for subdomain in subdomains]

        for future, subdomain in zip(futures, subdomains):
            http_status = future.result()
            https_status = check_subdomain_status(subdomain, "https")
            print(f"{subdomain}, http:{http_status}, https:{https_status}")


if __name__ == "__main__":
    main()
