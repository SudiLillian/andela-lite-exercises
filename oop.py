from datetime import datetime


class User(object):
    """docstring for User"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.date_joined = datetime.now()

    def __repr__(self):
        return "<User " + self.name + ">"


class Contribution(object):
    """docstring for Contributions"""
    def __init__(self, contributor, lines, repo):
        self.contributor = contributor  # GithubUser object
        self.lines = lines
        self.last_contribution = datetime.now()
        contributor.contributions.append(self)
        repo.contributions.append(self)

    def __repr__(self):
        return "<Contribution " + self.contributor.name + "-" + \
            str(self.last_contribution) + ">"


class Repository(object):
    """docstring for Repository"""
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator  # Github User
        self.contributions = []
        self.date_created = datetime.now()
        creator.repos.append(self)

    def __repr__(self):
        return "<Repo " + self.name + ">"


class GithubUser(User):
    """GithubUser is a User"""
    def __init__(self, name, email):
        super(GithubUser, self).__init__(name, email)
        self.repos = []
        self.contributions = []
        self.followers = []
        self.following = []

    def follow(self, user):
        """Follow another user : arg=User object"""
        user.followers.append(self)
        self.following.append(user)

    def __repr__(self):
        return "<Github user " + self.name + ", " +\
            self.email + ", " + str(self.date_joined) + ">"



stan = GithubUser("Stan", "stan@gmail.com")
amos = GithubUser("Amos", "amos@gmail.com")
joan = GithubUser("Joan", "joan@gmail.com")
srepo = Repository("repo1", stan)
contrib1 = Contribution(amos, 100, srepo)
stan.follow(joan)
stan.follow(amos)

print joan.followers
print stan.followers
print amos.followers
print joan.following
print stan.following
print amos.following
print srepo.contributions