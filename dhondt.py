class Party:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.discounted_votes = votes
        self.seats = 0
        
    def assign_seat(self):
        self.seats += 1
        self.discounted_votes = self.votes/(self.seats+1)        
        
    def print_info(self, all_seats, all_votes):
        print(self.name + ":")
        print(f'Votes: {self.votes} -> {self.votes/all_votes:.2%}')
        print(f'Seats: {self.seats} -> {self.seats/all_seats:.2%}')
        print(f'Votes per seat: {self.votes/self.seats:.2f}')
        print()
        
parties = [Party('PIS', 5711687),
           Party('PO', 3661474),
           Party('Kukiz15', 1339094),
           Party('Nowoczesna', 1155370),
           Party('PSL', 779875),
           Party('Mniejszosc Niemiecka', 27530)]

for i in range(460):
    chosen_party = max(parties, key=lambda p: p.discounted_votes)
    chosen_party.assign_seat()
    
all_votes = sum(p.votes for p in parties)

for party in parties:
    party.print_info(460, all_votes)
