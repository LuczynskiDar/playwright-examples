
from pages.base_page import BasePage

class TablesPage(BasePage):
    
    TABLE_LOCATOR = 'table#table1'
    
    def get_cell(self, row: int, col: int) -> str:
        table = self.page.locator(self.TABLE_LOCATOR)
        cell = table.locator('tbody tr').nth(row).locator('td').nth(col)
        cell_text = cell.inner_text()
        return cell_text.strip()
    
    def get_column_values(self, col: int) -> list[str]:
        table = self.page.locator(self.TABLE_LOCATOR)
        rows = table.locator('tbody tr')
        column_values = []
        for i in range(rows.count()):
            column = rows.nth(i).locator('td')
            column_values.append(column.nth(col).inner_text().strip())
        return column_values
    
