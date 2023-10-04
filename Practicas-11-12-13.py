
import flet as ft
import random

class Matriz:
   def __init__(self) -> None:
      pass
   def random_matriz(self, rows, cols,a,b):
      matriz = []
      for i in range(rows):
         matriz.append([])
         for j in range(cols):
            matriz[i].append(random.randint(a,b))
      return matriz
   
   def sum(self, matriz):
      rows = len(matriz)
      cols = len(matriz[0])
      matriz_sum = {
         "Sum_Rows": [],
         "Sum_Cols": [],
         "Avg_Rows": [],
         "Avg_Cols": [],
         "Total_sum": 0
      }

      for i in range(rows):
        matriz_sum["Sum_Rows"].append(sum(matriz[i]))
        matriz_sum["Avg_Rows"].append(round(matriz_sum["Sum_Rows"][i]/cols,2))
    
      for i in range(cols):
        matriz_sum["Sum_Cols"].append(0)
        for j in range(rows):
            matriz_sum["Sum_Cols"][i] += matriz[j][i]
        matriz_sum["Avg_Cols"].append(round(matriz_sum["Sum_Cols"][i]/rows,2))

      matriz_sum["Total_sum"] = sum(matriz_sum["Sum_Rows"])

      return matriz_sum
   def max_sale(self, matriz):
      sale = {
         "Number_Sale": 0,
         "Day": "",
         "Month": ""
      }
      Days = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
      Months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
      for i in range(len(matriz)):
         for j in range(len(matriz[i])):
            if matriz[i][j] >= sale["Number_Sale"]:
               sale["Number_Sale"] = matriz[i][j]
               sale["Day"] = Days[j]
               sale["Month"] = Months[i]
      return sale
   def min_sale(self, matriz):
      sale = {
         "Number_Sale": 9999,
         "Day": "",
         "Month": ""
      }
      Months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
      Days = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
      for i in range(len(matriz)):
         for j in range(len(matriz[i])):
            if matriz[i][j] <= sale["Number_Sale"]:
               sale["Number_Sale"] = matriz[i][j]
               sale["Day"] = Days[j]
               sale["Month"] = Months[i]
      return sale
   def get_below_of(self,matriz, num_to_compare):
      exam_fail = {
       "Parcial 1": 0,
       "Parcial 2": 0,
       "Parcial 3": 0
      }
      rows = len(matriz)
      cols = len(matriz[0])
      for i in range(cols):
        for j in range(rows):
           if matriz[j][i] < num_to_compare:
              exam_fail[f"Parcial {i+1}"] += 1
      return exam_fail
   
   def get_final_grades(self, matriz):
      list = {
       "0 - 4.9": 0,
       "5 - 5.9": 0,
       "6 - 6.9": 0,
       "7 - 7.9": 0,
       "8 - 8.9": 0,
       "9 - 10": 0,
      }
      n = len(matriz)
      for i in range(n):
         if matriz[i] <= 4.9:
            list["0 - 4.9"] += 1
         if matriz[i] > 4.9 and matriz[i] <= 5.9:
            list["5 - 5.9"] += 1
         if matriz[i] > 5.9 and matriz[i] <= 6.9:
            list["6 - 6.9"] += 1
         if matriz[i] > 6.9 and matriz[i] <= 7.9:
            list["7 - 7.9"] += 1
         if matriz[i] > 7.9 and matriz[i] <= 8.9:
            list["8 - 8.9"] += 1
         if matriz[i] > 8.9 and matriz[i] <= 10:
            list["9 - 10"] += 1
      return list
   def max_avg(self, matriz):
      value = 0
      for item in matriz:
         if item > value:
            value = item
      return value
   def min_avg(self, matriz):
      value = 11
      for item in matriz:
         if item < value:
            value = item
      return value
def main(page: ft.Page):
  def print_matriz_sum(matriz, sum_matriz, titulo):
    container_matriz = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=500)
    body_container = ft.Container(container_matriz,width=700)
    main_container = ft.Column([
       ft.Text(f"{titulo}", size=30, weight="bold"), 
       body_container
    ])
    
    rows = len(matriz)
    cols = len(matriz[0])
    for i in range(rows):
      container_matriz.controls.append(ft.Row(spacing=10))
      for item in matriz[i]:
        container_matriz.controls[i].controls.append(ft.Container(ft.Text(item),alignment=ft.alignment.center,width=40))
      container_matriz.controls[i].controls.append(ft.Container(ft.Text(sum_matriz["Sum_Rows"][i]),alignment=ft.alignment.center,width=40,margin=ft.margin.only(left=40)))
      container_matriz.controls[i].controls.append(ft.Container(ft.Text(sum_matriz["Avg_Rows"][i]),alignment=ft.alignment.center,width=40))

      container_matriz.controls.append(ft.Row(spacing=10))
      container_matriz.controls.append(ft.Row(spacing=10))

    for j in range(cols):
       container_matriz.controls[rows].controls.append(ft.Container(ft.Text(sum_matriz["Sum_Cols"][j]),alignment=ft.alignment.center,width=40,margin=ft.margin.only(top=40)))
       container_matriz.controls[1+rows].controls.append(ft.Container(ft.Text(sum_matriz["Avg_Cols"][j]),alignment=ft.alignment.center,width=40))
    
    return main_container
  
  def print_matriz_sales(matriz_print, sum_matriz, titulo):
    Days = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
    container_matriz = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=500)
    body_container = ft.Container(container_matriz,width=250)
    min_max_sales = ft.Column(height=500)
    main_container = ft.Column([
       ft.Text(f"{titulo}", size=30, weight="bold"), 
       ft.Row([body_container,min_max_sales])
    ])
    
    rows = len(matriz_print)
    for i in range(rows):
      container_matriz.controls.append(ft.Row(spacing=10))
      for item in matriz_print[i]:
        container_matriz.controls[i].controls.append(ft.Container(ft.Text(item),alignment=ft.alignment.center,width=40))

    max_sale = matriz.max_sale(matriz_print)
    min_sale = matriz.min_sale(matriz_print)

    min_max_sales.controls.append(ft.Container(ft.Text(f"La mayor venta fue de ${max_sale['Number_Sale']} los {max_sale['Day']} de {max_sale['Month']}"),alignment=ft.alignment.center,width=150,margin=ft.margin.only(left=40)))
    min_max_sales.controls.append(ft.Container(ft.Text(f"La menor venta fue de ${min_sale['Number_Sale']} los {min_sale['Day']} de {min_sale['Month']}"),alignment=ft.alignment.center,width=150,margin=ft.margin.only(left=40)))
    min_max_sales.controls.append(ft.Container(ft.Text(f"La venta total del año es de ${sum_matriz['Total_sum']}"),alignment=ft.alignment.center,width=150,margin=ft.margin.only(left=40)))
    min_max_sales.controls.append(ft.Container(ft.Column(width=150),alignment=ft.alignment.center,width=150,margin=ft.margin.only(left=40)))

    for i in range(len(matriz_print[0])):
       min_max_sales.controls[3].content.controls.append(
          ft.Text(f"{Days[i]}: ${sum_matriz['Sum_Cols'][i]}")
       )
    
    return main_container
  
  def print_matriz_grades(matriz_print, sum_matriz, below_matriz, titulo):
    resultados.width = 500
    container_matriz = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=400)
    body_container = ft.Container(container_matriz,width=500)
    main_container = ft.Column([
       ft.Text(f"{titulo}", size=30, weight="bold"),
       ft.Row([body_container])
    ])
    
    rows = len(matriz_print)
    for i in range(rows):
      container_matriz.controls.append(ft.Row(spacing=10))
      for item in matriz_print[i]:
        container_matriz.controls[i].controls.append(ft.Container(ft.Text(item),alignment=ft.alignment.center,width=100))
      container_matriz.controls[i].controls.append(ft.Container(ft.Text(sum_matriz["Avg_Rows"][i]),alignment=ft.alignment.center,width=100))

    container_matriz.controls.append(ft.Row(spacing=10))
    for i in range(len(matriz_print[0])):
       fail_exam = below_matriz[f'Parcial {i+1}']
       container_matriz.controls[rows].controls.append(ft.Container(ft.Text(f"Parciales reprobados: {fail_exam}"),alignment=ft.alignment.center,width=100,margin=ft.margin.only(top=10)))

    container_matriz.controls.append(ft.Row(spacing=10))
    container_matriz.controls[rows+1].controls.append(ft.Container(ft.Text(f"Total de parciales reprobados: {fail_exam}"),alignment=ft.alignment.center,width=100))

    final_grades = matriz.get_final_grades(sum_matriz["Avg_Rows"])
    container_matriz.controls[rows+1].controls.append(ft.Column())
    for i,item in final_grades.items():
       container_matriz.controls[rows+1].controls[1].controls.append(ft.Text(f"{i}: {item}"))

    container_matriz.controls[rows+1].controls.append(ft.Column())
    container_matriz.controls[rows+1].controls[2].controls.append(ft.Text(f"Promedio más alto: {matriz.max_avg(sum_matriz['Avg_Rows'])}"))
    container_matriz.controls[rows+1].controls[2].controls.append(ft.Text(f"Promedio más bajo: {matriz.min_avg(sum_matriz['Avg_Rows'])}"))
   
    return main_container
           
  def handle_sum_rand_numbers(e):
     res_matriz = matriz.random_matriz(2,3,0,20)
     sum_matriz = matriz.sum(res_matriz)
     resultados.content = print_matriz_sum(res_matriz,sum_matriz,"Matriz")
     page.update()
  def handle_sales(e):
     res_matriz = matriz.random_matriz(12,5,0,100)
     sum_matriz = matriz.sum(res_matriz)
     resultados.content = print_matriz_sales(res_matriz,sum_matriz,"Ventas")
     page.update()
  def handle_grades(e):
     res_matriz = matriz.random_matriz(8,3,0,10)
     below_matriz = matriz.get_below_of(res_matriz,7)
     sum_matriz = matriz.sum(res_matriz)
     resultados.content = print_matriz_grades(res_matriz,sum_matriz,below_matriz,"Calificaciones")
     page.update()
  def handle_change_interface(e):
    resultados.width = 300
    page.controls.clear()
    resultados.content.clean()
  
    if menu_options.value == "Números aleatorios":
        title.value = "Números aleatorios"
        btn_cal.on_click=handle_sum_rand_numbers
    if menu_options.value == "Resumen ventas":
        title.value = "Resumen ventas"
        btn_cal.on_click=handle_sales
    if menu_options.value == "Calificaciones":
        title.value = "Calificaciones"
        btn_cal.on_click=handle_grades
    
    page.add(container)

  matriz = Matriz()
  menu_options = ft.Dropdown(options=[
        ft.dropdown.Option("Números aleatorios"),
        ft.dropdown.Option("Resumen ventas"),
        ft.dropdown.Option("Calificaciones")
    ], width=350,value="Números aleatorios", border_color="#2267a8", border_width=5, on_change=handle_change_interface)
  btn_cal = ft.ElevatedButton("Resultados", on_click=handle_sum_rand_numbers)
  title = ft.Text("Números aleatorios",size=20,weight="bold")
  resultados = ft.Container(ft.Text(),width=300)

  container = ft.Container(
      ft.Column([
          title, menu_options, btn_cal,resultados]),alignment=ft.alignment.center,
          margin=25)
  
  page.add(container)

ft.app(main)