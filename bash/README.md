```bash
comm -123 <(sort old) <(sort new) # не выводить: 1 уникальные файлы для старого, 2 нового; 3 общие для обоих
echo 'command'|at HH:MM # выполнить команду в определённой время (через cron)
```