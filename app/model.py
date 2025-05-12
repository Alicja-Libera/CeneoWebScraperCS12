class Product:
    def __init__(self):
        pass

class Opinion:
    selectors = {

    }
    def __init_(self, opinion_id, author, recommend, stars, content, pros, cons, up_votes, down_votes, published, purchased ):
        self.opinion_id = opinion_id
        self.author = author
        self.recommend = recommend
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.up_votes = up_votes
        self.down_votes = down_votes
        self.published = published
        self.purchased = purchased

    def __str__(self): 
        return "\n".join([f"{key}: {getattr(self,key)}" for key in self.selectors.keys()]
    def __repr__(self):
        return "Opinions("+", ".join[f"{key}: {getattr(self,key)}" for key in self.selectors.keys()] +")"
