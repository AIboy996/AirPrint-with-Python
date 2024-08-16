# AirPrint-with-Python
A **virtual, local-hosted** AirPrint server powerd by Python.

You can **send pdf file from Apple devices** to the server via AirPrint protocol.

>[!TIP] 
> What's AirPrint?
> 
> AirPrint is an Apple technology that helps you create full-quality printed output without the need to download or install drivers.
> 
> With AirPrint, it’s easy to deliver photo and document printing in your iOS apps and macOS apps without the need to download or install drivers. AirPrint is built into most popular printer models and offers a complete set of features, including full-quality output, automatic media selection, and enterprise-class finishing options.

## How AirPrint-with-Python Works?

### Step 1
Add a `virtual TCP printer` in your Operating System by hand:

- [on Windows10/11?](https://sscs.uchicago.edu/add-network-printer-windows10/)
- on MacOS?
- on Linux?

### Step 2
Start a `TCP server` to receive data in PostScript format.

### Step 3
Convert `.ps` to `.pdf` with **ps2pdf**(usually installed with TeX, such as [MiKTeX](https://miktex.org/)) automaticly.

## References

- [AirPrint Apple Support](https://support.apple.com/en-us/HT201311)
- [AirPrint Apple Developer](https://developer.apple.com/airprint/)
- [将Windows 上的打印机共享为AirPrint - Jiaxin's Blog](https://shoujiaxin.github.io/2018/12/02/将-Windows-上的打印机共享为-AirPrint/)
- [Air Printer - 隔空打印机服务器](https://apps.apple.com/cn/app/air-printer-隔空打印机服务器/id929399895)
- [RWTS-PDFwriter](https://github.com/rodyager/RWTS-PDFwriter)
- [AirPdfPrinter](https://github.com/thyrlian/AirPdfPrinter.git)