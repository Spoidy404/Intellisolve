from pydantic import BaseModel

class ImageData(BaseModel):
    image: str
    dict_of_vars: dict
def find_greatest(numbers):
    greatest = numbers[0]

    for num in numbers:
        if num > greatest:
            greatest = num

    return greatest


numbers = [10, 45, 23, 67, 32]

result = find_greatest(numbers)

print("Greatest number:", result)



