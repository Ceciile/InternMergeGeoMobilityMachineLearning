import osmium as osm
import pandas as pd

class TimelineHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.elemtimeline = []

    def node(self, n):
        self.elemtimeline.append(["node",
                                  n.id,
                                  n.version,
                                  n.visible,
                                  pd.Timestamp(n.timestamp),
                                  n.uid,
                                  n.changeset,
                                  len(n.tags)])

tlhandler = TimelineHandler()
tlhandler.apply_file("../../Downloads/rhone-alpes-latest.osm.pbf")
colnames = ['type', 'id', 'version', 'visible', 'ts', 'uid', 'chgset', 'ntags']
elements = pd.DataFrame(tlhandler.elemtimeline, columns=colnames)
elements = elements.sort_values(by=['type', 'id', 'ts'])
elements.head(10)