# Subdomain Status Code Finder

A Python tool for enumerating the HTTP status codes of subdomains using a wordlist.

## Overview

Subdomain Status Code Finder is a simple Python script that allows you to quickly check the HTTP status codes of multiple subdomains using a list of potential subdomains. It's a useful tool for security professionals, penetration testers, and web developers who need to identify active subdomains and assess their response.

This tool leverages the popular requests library to send HTTP requests to subdomains and collect their status codes. By providing a wordlist of subdomains to the script, you can efficiently scan and gather information about various subdomains, helping you in tasks like security assessments, subdomain enumeration, or troubleshooting.

<h3>Features</h3>
<ul>
  <li><b>Parallel Scanning</b>: Subdomain Status Code Finder uses Python's concurrent.futures to execute HTTP requests in parallel, making the scanning process faster and more efficient.</li>
  <li><b>HTTP and HTTPS Support</b>: The script can check the status codes for both HTTP and HTTPS protocols, providing a comprehensive view of the subdomains' accessibility.</li>
  <li><b>Custom Wordlist:</b> You can easily provide your own wordlist of subdomains, allowing you to customize the scanning process for your specific needs.</li>
  <li><b>Detailed Output:</b> The tool provides detailed output, including the subdomain name and its corresponding HTTP and HTTPS status codes, making it easy to analyze the results.</li>
</ul>

<h3>Usage</h3>
1.Clone the repository to your local machine.

2.Run the Python script:
<code>python subdomain_status_finder.py</code>

3.enter your custom subdomain wordlist name.

The script will execute HTTP and HTTPS requests for each subdomain in parallel and display the status codes.


<code>enter your subdomain file name:sub_domain_wordlist.txt</code>
<br><br>
<code>subdomain1.example.com, http:200, https:301</code><br>
<code>subdomain2.example.com, http:403, https:403</code><br>
<code>subdomain3.example.com, http:200, https:200</code><br>


