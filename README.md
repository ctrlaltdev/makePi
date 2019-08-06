[![License](https://img.shields.io/github/license/ctrlaltdev/makePi?style=for-the-badge)](https://github.com/ctrlaltdev/makePi/blob/master/LICENSE)
![Python](https://img.shields.io/badge/_-Python-4B8BBE.svg?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/_-JS-F0DB4F.svg?style=for-the-badge)

A Pi API: https://pi.ctrlalt.dev/

## Endpoints:
### GET
| Path | Returns | curl |
| --- | --- | --- |
| `/` | Pi with 100 decimals | `curl https://pi.ctrlalt.dev/` |
| `/<n>` | Pi with n decimals | `curl https://pi.ctrlalt.dev/10` |
| `/decimals/` | Pi 100 first decimals | `curl https://pi.ctrlalt.dev/decimals/` |
| `/decimals/<n>` | Pi n first decimals | `curl https://pi.ctrlalt.dev/decimals/10` |
| `/stream` | Stream of Pi decimals with a 500ms delay | `curl https://pi.ctrlalt.dev/stream` |
| `/stream/<t>` | Stream of Pi decimals with a t ms delay | `curl https://pi.ctrlalt.dev/stream/1000` |

All endpoints but `stream` return json  
