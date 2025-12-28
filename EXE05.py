import tkinter as tk
# print('=' * 50)
# print('AVALIAÇÃO DO ALUNO 📚'.center(50))
# print('=' * 50)

window = tk.Tk()
window.title("Calculadora de Aprovação")
window.geometry("400x300")

text = tk.Label(window, text="AVALIAÇÃO DO ALUNO")
text.pack()

tk.Label(window, text="Digite a primeira nota:").pack()
nota1 = tk.Entry(window)
nota1.pack()
tk.Label(window, text="Digite a segunda nota:").pack()
nota2 = tk.Entry(window)
nota2.pack()


# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))

# media = (nota1 + nota2) / 2
text_n1 = tk.Label(window, text=f"Notas informadas:")
text_n1.pack()
text_n2 = tk.Label(window, text=f"Média final:")
text_n2.pack()

situacao = tk.Label(window, text="Situação:")
situacao.pack()

media = 0

def btn():
    n1 = int(nota1.get())
    n2 = int(nota2.get())
    media = ((n1 + n2) / 2)
    text_n1['text'] = f"Notas informadas: {n1:.2f} e {n2:.2f}"
    text_n2['text'] = f"Média final: {media:.2f}"
    if media >= 7:
        # print('✅ Situação: APROVADO')
        situacao['text'] = "Situação: APROVADO"
    elif media >= 5:
        # print('⚠️ Situação: RECUPERAÇÃO')
        situacao['text'] = "Situação: RECUPERAÇÃO"
    else:
        # print('❌ Situação: REPROVADO')
        situacao['text'] = "Situação: REPROVADO"


tk.Button(window, text="Calcular", command=btn).pack()

# print('-' * 50)
# print(f'Notas informadas: {nota1:.2f} e {nota2:.2f}')
# print(f'Média final: {media:.2f}')
# print('-' * 50)


# print('=' * 50)

window.mainloop()