# AirPrint-with-Python
A local AirPrint server powerd by Python.

## What's AirPrint?
AirPrint is an Apple technology that helps you create full-quality printed output without the need to download or install drivers.

> For more infomation [check Apple Support](https://support.apple.com/en-us/HT201311)

## How AirPrint-with-Python Works?

### receive printed data in PostScript format
Package `socketserver` provide a easy to set up a local TCP server.
### convert .ps to .pdf
Use `GhostScript`

---

## References
[将Windows 上的打印机共享为AirPrint - Jiaxin's Blog](https://shoujiaxin.github.io/2018/12/02/%E5%B0%86-Windows-%E4%B8%8A%E7%9A%84%E6%89%93%E5%8D%B0%E6%9C%BA%E5%85%B1%E4%BA%AB%E4%B8%BA-AirPrint/)
[RWTS-PDFwriter](https://github.com/rodyager/RWTS-PDFwriter)
[Air Printer - 隔空打印机服务器](https://apps.apple.com/cn/app/air-printer-%E9%9A%94%E7%A9%BA%E6%89%93%E5%8D%B0%E6%9C%BA%E6%9C%8D%E5%8A%A1%E5%99%A8/id929399895)