import whois
import multiprocessing

tld = "it"

def check_available(domain: str) -> tuple[str, bool]:
    print(f"Checking {domain}")
    try:
        whois.whois(domain)
        return (domain, False)
    except whois.exceptions.WhoisDomainNotFoundError:
        return (domain, True)
    except whois.exceptions.WhoisError:
        return (domain, False)
    except Exception as e:
        print(e)
        return (domain, False)


if __name__ == "__main__":
    tlds = ["de", "cn", "uk", "eu", "nl", "in", "it", "ch", "es", "be", "hu", "au", "us", "im", "re", "fr", "pm", "tf", "yt", "wf", "li"]
    words = ["xhost"]
    results = []

    domains = []

    for tld in tlds:
        for word in words:
            domains.append(f"{word}.{tld}")

    with multiprocessing.Pool(processes=6) as pool:
        values = pool.map(check_available, (domain for domain in domains), chunksize=5)
        results.append(values)

    print("Available domains:")

    for c in results:
        for i in c:
            if i[1] == True:
                print(i[0])
