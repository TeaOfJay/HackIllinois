from user_data.models import user_data
u = user_data(user_id = "1234asdf", first_name = "Ryan", last_name = "Gontarek", interests = "MemesOfJonathan")
u.save()
print(u.first_name)
