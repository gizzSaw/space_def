class Stats: 
    """отслеживание статистики"""

    def __init__(self):
        """инициализация класса"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """статистика изменяющаяся во время игры"""
        self.guns_left = 2
        self.score = 0