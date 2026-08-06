# OS-Setup
A bash script to setup my new Linux installs with my pre-configured options and preferred packages.
Please keep in mind this is meant for personal use as a hobby project, I am in no way a professional software engineer. If you want to take this and adapt it for your use, please refer to the [LICENSE](https://github.com/CraftierBark8/OS-Setup/blob/main/LICENSE).

## ⌨️ Usage
1. Install python3 & git. On newer distros, this may be pre-installed
2. Clone the repo
3. Open repo
4. Use wget or curl to add the 3rd party dependencies
3. Execute 'setup.py' to start

**For Ubuntu**
```bash
sudo apt install git python3
git clone https://github.com/CraftierBark8/OS-Setup.git
cd ./OS-Setup
curl -O https://raw.githubusercontent.com/python-distro/distro/master/src/distro/distro.py
python3 ./setup.py
```
## ✨ Features ✨

- [soon] Dynamic installs with .json files
- [soon] Pre-made config support
- More to come!

## 🛠️ OS Support

Currently I am only targeting popular Ubuntu based distros (ones that support apt) but more may come.

## 📄 Documentation

Documentation for the different modules and functions is available in [documentation.md](https://github.com/CraftierBark8/OS-Setup/blob/main/documentation.md).

## ✏️ Contributing

This is a personal hobby project so contributions will likely go answered for now. I only work on this when I feel like it or have a problem with it. Similarly, I am not using or active with GitHub issue tracking.

## ⚖️ License

GNU Affero General Public License 3.0
See [LICENSE](https://github.com/CraftierBark8/OS-Setup/blob/main/LICENSE) for details.

## ❤️ Credits

Thank you to the all the software I use in my day-to-day. For a full list of software installed with this config and links, see [documentation.md](https://github.com/CraftierBark8/OS-Setup/blob/main/documentation.md)