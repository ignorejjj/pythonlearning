import pdfkit
import time

def url_to_pdf(url,to_file):
    
    path_wkthmltopdf = r'E:\软件\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_url(url, to_file, configuration=config)
    print('完成')

print("请输入要保存的链接:",end='')
url=input()
print("请输入保存的文件名:",end='')
name=input()
url_to_pdf(url, name+'.pdf')
time.sleep(100)