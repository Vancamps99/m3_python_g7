from string import Template
html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <meta charset="UTF-8">
                            <title>Aves </title>
                            </head>
                            <body>
                            <h1>Aves chile</h1>
                            $body
                            </body>
                            </html>
                            ''')
aves_template=Template(''' <h2>$nom_esp</h2>
                           <h2>$nom_ing</h2>
                           <img src="$img "alt="imagen" >'''                       
                          )
