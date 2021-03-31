Feature: Chek catalog
Scenario: Write potom
  Given website "https://abctica.com/ru"
  Then click on href with text 'Пищевые продукты'
  Then click on href with text 'Клубника Турция'
  Then push button with text 'В корзину'
  Then click on href with text 'Перейти в корзину'
  Then page include text 'Клубника Турция'