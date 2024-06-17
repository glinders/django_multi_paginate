
### Python version
```
python --version
Python 3.12.4
```
See `requirements.txt` for necessary packages.

### github  gnutls_handshake() failed: Error in the pull function.

See https://github.com/microsoft/WSL/issues/5346#issuecomment-1016469312

gist:
```
The problem was in a mismatch between VPN MTU and Linux under WSL2 MTU sizes.

It can be identified via 2 commands:

Windows PowerShell (run as administrator)

netsh interface ipv4 show subinterfaces

Notice the first row - it shows how big MTU is allowed in your VPN.

Linux (inside WSL2) console

ip addr

Notice the row starting 'eth0' - its MTU must match or be lower that the one above.

In my case the MTU in Linux was higher.

Solution

The following command instantly solves the problem:

sudo ip link set dev eth0 mtu 1400 (update MTU value to fit your VPN)

```