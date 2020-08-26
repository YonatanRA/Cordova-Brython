from browser import document, alert, bind


del_all_button = document['del_all']
del_one_button = document['del_one']
calc_button = document['calcular']
other_buttons = [btn for btn in document.select('button') if btn not in (del_all_button, del_one_button, calc_button)]
resultado = document['resultado']



def other_button_click(e):

    if resultado.text == '0':
        resultado.text = ''

    resultado.text = resultado.text + e.target.text

    if resultado.text.startswith('x') or resultado.text.startswith('/'):
        resultado.text = '0'


for btn in other_buttons:
    btn.bind('click', other_button_click)



@bind(calc_button, 'click')
def calcular(e):

    operacion = resultado.text
    operacion_python = operacion.replace('x', '*').replace(',', '.')

    try:
        calculo = eval(operacion_python)
        calculo = round(calculo, 2)
        resultado.text = str(calculo).replace('.', ',')

    except:
        alert(f'Error de Cálculo:\n\n {resultado.text} = ?')
        resultado.text = '0'



@bind(del_all_button, 'click')
def del_all(e):
    resultado.text = '0'



@bind(del_one_button, 'click')
def del_one(e):

    if len(resultado.text) == 1:
        resultado.text = '0'

    else:
        resultado.text = resultado.text[:-1]
