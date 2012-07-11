from coderwall import CoderWall
from tahrir_api.dbapi import TahrirDatabase
import sys


def usage():
    print "cw2ob: dburi cw-username ob-email"

def main():
    if len(sys.argv) < 4:
        usage()
        exit()
    db = TahrirDatabase(sys.argv[1])
    issuer_id = db.add_issuer(
            "http://coderwall.com",
            "coderwall",
            "http://coderwall.com",
            "support@coderwall.com"
            )
    db.add_person(hash(sys.argv[3]), sys.argv[3])
    cw = CoderWall(sys.argv[2])
    for badge in cw.badges:
        db.add_badge(
                badge.name,
                badge.image_uri,
                badge.description,
                "http://coderwall.com",
                issuer_id)
        db.add_assertion(
                badge.name.lower(),
                sys.argv[3],
                None
                )

    print "Awarded {0} badges to {1}".format(len(cw.badges), sys.argv[3])
