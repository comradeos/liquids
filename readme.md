# Liquids API
Python/Flask based API with SQL database storage and SQLAlchemy connection  

### Build project
```
docker exec -it liquids-python-1 sh  
```
```
project address http://127.0.0.1:5003/  
```

### Python interactive mode
```
docker exec -it liquids-python-1 python  
```

### Database actions 
```
from logic import db
```
```
from data import Drink
```
```
item = Drink(id=None, name="Liqtest", description="Test description")
```
```
db.session.add(item)
```
```
db.session.commit()
```
