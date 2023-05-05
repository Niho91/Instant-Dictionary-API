import justpy as jp


class Doc():

    def serve(self):
        wp = jp.WebPage()


        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=div, text="Instant dictionary API!", classes="text.4xl m-2")
        jp.Div(a=div, text="Get definitions of words!", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="web addres where u deploy api www.exaple.com/api?w=moon")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        word and a definition in jason
        """)
        return wp

