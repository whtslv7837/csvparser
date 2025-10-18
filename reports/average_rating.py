from collections import defaultdict


class AverageRatingReport:
    def __init__(self, data):
        self.data = data


    def generate(self):
        brand_rating = defaultdict(list)

        for row in self.data:
            brand = row.get('brand')
            rating = float(row.get('rating'))

            if brand:
                brand_rating[brand].append(rating)

        averages = [
            (brand, round(sum(rating) / len(rating), 2))
            for brand, rating in brand_rating.items()
        ]

        return sorted(averages, key=lambda x: x[1], reverse=True)

