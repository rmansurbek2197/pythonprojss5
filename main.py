class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        raise StopIteration

def generate_data(size):
    for i in range(size):
        yield i * 2

def process_data(data):
    processed_data = []
    for item in data:
        processed_data.append(item + 10)
    return processed_data

def main():
    data_size = 1000000
    data_generator = generate_data(data_size)
    data_processor = DataProcessor(process_data(data_generator))
    for _ in range(10):
        print(next(data_processor))

if __name__ == "__main__":
    main()