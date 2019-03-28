#-*-coding:utf-8-*-



#页面的主要文本，其中name和products是动态部分
PAGE_HTML="""
<p>Welcome,{name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>
"""

#商品项的主要文本，prodname 与 price 是动态部分
PRODUCT_HTML="<li>{productname}:{price}</li>\n"

def make_page(usernaem,products):
    #存储商品列表文本
    product_html=""
    for prodname,price in products:
        product_html+=PRODUCT_HTML.format(
            prodname=prodname,price=format_price(price)
        )
    html=PAGE_HTML.format(name=usernaem,products=product_html)
    return html

def format_price(price):
    return price

def main():
    pass

if __name__ == '__main__':
    main()