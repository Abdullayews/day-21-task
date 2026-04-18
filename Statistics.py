class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        total = 0
        for x in self.data:
            total += x
        return total

    def min(self):
        minimum = self.data[0]
        for x in self.data:
            if x < minimum:
                minimum = x
        return minimum

    def max(self):
        maximum = self.data[0]
        for x in self.data:
            if x > maximum:
                maximum = x
        return maximum

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count(), 1)

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        frequency = {}
        for x in self.data:
            frequency[x] = frequency.get(x, 0) + 1
        max_count = max(frequency.values())
        for value, count in frequency.items():
            if count == max_count:
                return (value, max_count)

    def var(self):
        m = self.mean()
        total = 0
        for x in self.data:
            total += (x - m) ** 2
        return round(total / self.count(), 1)

    def std(self):
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        frequency = {}
        for x in self.data:
            frequency[x] = frequency.get(x, 0) + 1
        n = self.count()
        result = []
        for value, count in frequency.items():
            percentage = round((count / n) * 100, 1)
            result.append((percentage, value))
        result.sort(reverse=True)
        return result

    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Variance: ', self.var())
        print('Standard Deviation: ', self.std())
        print('Frequency Distribution:', self.freq_dist())


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()
