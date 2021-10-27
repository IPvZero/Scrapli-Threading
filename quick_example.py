"""
pip install scrapli
pip install rich

"""

from concurrent.futures import ThreadPoolExecutor

from rich import print as rprint
from scrapli.driver.core import IOSXEDriver

from inv import DEVICES

def send_cmd(device):
    """Scrapli all the things"""
    
    hostname = device["hostname"]
    with IOSXEDriver(
        host=device["host"],
        auth_username="john", #my home lab credentials
        auth_password="cisco", #change these to fit your needs
        auth_strict_key=False,
        ssh_config_file=True,
    ) as conn:
        response = conn.send_command("show ip interface brief")
        return hostname, response.result

if __name__ == "__main__":

    with ThreadPoolExecutor() as executor:
        results = executor.map(send_cmd, DEVICES)

    for result in results:
        rprint(f"\n\n[cyan]==== {result[0]} ====[/cyan]")
        rprint(result[1])
