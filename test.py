from fpdf import FPDF


class LableUnoA5(FPDF):
    def header(self):
        # Добавляем текст в определенные места на этикетке 1
        self.image('assets/images/uno.png', x=20, y=20, w=436 / 5, h=290 / 5)
        self.set_draw_color(150)
        self.set_line_width(0.75)
        self.line(x1=20, y1=90, x2=107, y2=90)
        self.set_xy(20, 150)
        self.image('assets/images/garbage.png', x=35, y=100, w=16 / 1.5, h=16 / 1.5)
        self.image('assets/images/Temperature.png', x=60, y=100, w=16 / 1.5, h=16 / 1.5)
        self.image('assets/images/company.png', x=85, y=100, w=16 / 1.5, h=16 / 1.5)

        # Добавляем текст в определенные места на этикетке 2
        self.image('assets/images/uno.png', x=20, y=170, w=436 / 5, h=290 / 5)
        self.set_draw_color(150)
        self.set_line_width(0.75)
        self.line(x1=20, y1=240, x2=107, y2=240)
        self.set_xy(20, 150)
        self.image('assets/images/garbage.png', x=35, y=250, w=16 / 1.5, h=16 / 1.5)
        self.image('assets/images/Temperature.png', x=60, y=250, w=16 / 1.5, h=16 / 1.5)
        self.image('assets/images/company.png', x=85, y=250, w=16 / 1.5, h=16 / 1.5)

    def top_right(self, number, charge, nettogewicht, versanddatum, ):
        # Добавляем текст в определенные места на этикетке 1
        self.set_font('helvetica', 'B', 36)
        self.set_xy(125, 25)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{number}', align="C")

        self.set_font('helvetica', 'B', 14)
        self.set_xy(125, 50)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Batch No:', align="L")
        self.set_xy(160, 50)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{charge}', align="L")
        self.set_xy(125, 60)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Net Weight:', align="L")
        self.set_xy(160, 60)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{nettogewicht} kg', align="L")
        self.set_xy(125, 70)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Date of Mfg:', align="L")
        self.set_xy(160, 70)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{versanddatum}', align="L")
        self.set_font('helvetica', 'B', 12)

        # Добавляем текст в определенные места на этикетке 2
        self.set_font('helvetica', 'B', 36)
        self.set_xy(125, 175)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{number}', align="C")
        self.set_font('helvetica', 'B', 14)
        self.set_xy(125, 200)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Batch No:', align="L")
        self.set_xy(160, 200)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{charge}', align="L")
        self.set_xy(125, 210)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Net Weight:', align="L")
        self.set_xy(160, 210)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{nettogewicht} kg', align="L")
        self.set_xy(125, 220)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Date of Mfg:', align="L")
        self.set_xy(160, 220)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{versanddatum}', align="L")

    def end_right(self):
        # Добавляем картинки справа на этикетке 1
        # self.set_font('helvetica', 'B', 6)
        self.set_font('DejaVu', size=9)
        self.set_xy(120, 100)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(
                80, 5,
                'Storage in closed original packaging at +10 - +30 °C Do not store below 0°C\n\n'
                'The glue should be stored in places protected from heat sources and direct sunlight\n', align="C"
                )
        self.set_xy(120, 250)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(
                80, 5,
                'Storage in closed original packaging at +10 - +30 °C Do not store below 0°C\n\n'
                'The glue should be stored in places protected from heat sources and direct sunlight\n', align="C"
                )

    def contour(self):
        # Контур этикетки 1
        self.set_line_width(10)
        self.set_draw_color(165)
        # self.line(x1=15, y1=197, x2=282, y2=197)
        self.rect(1, 1, 210, 140, style="D")
        self.line(x1=0, y1=148.5, x2=210, y2=148.5)
        self.set_draw_color(15)

        # Контур этикетки 2
        self.set_line_width(10)
        self.set_draw_color(165)
        self.rect(1, 152, 210, 140, style="D")

        # Черная линия разреза
        self.set_line_width(1)
        self.set_draw_color(0, 0, 0)
        self.line(x1=0, y1=148.5, x2=210, y2=148.5)


def main():
    # Создаем экземпляр класса PDF

    pdf = LableUnoA5()  # Устанавливаем альбомную ориентацию (L - landscape) number, charge, nettogewicht, versanddatum
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.end_right()
    # Добавляем содержимое и картинки
    pdf.contour()
    pdf.top_right("699 P", '052301', "20  ", "01.12.2023")
    # Сохраняем PDF-файл
    pdf.output(fr'./test.pdf')


if __name__ == '__main__':
    main()
