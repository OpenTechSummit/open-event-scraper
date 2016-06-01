class Track(object):
    id = 0
    header_line = 1
    filename = ""
    key_color = "#FF4D55"
    name = ""
    description = ""
    track_image_url = "http://lorempixel.com/400/200"
    location = ""
    gid = ""
    order = -1

    def __init__(self, id, name, header_line, key_color, location, gid, order):
        super(Track, self).__init__()
        self.id = id
        self.name = name
        self.header_line = header_line
        self.key_color = key_color
        self.track_image_url = "http://lorempixel.com/400/200"
        self.location = location
        self.gid = gid
        self.order = order

class Service(object):
    id = 0
    service = ""
    url = ""

    def __init__(self, id, service, url):
        super(Service, self).__init__()
        self.id = id
        self.service = service
        self.url = url


class LogoIco(object):
    logo_url = ""
    ico_url = ""
    main_page_url = ""

    def __init__(self, logo_url, ico_url, main_page_url):
        super(LogoIco, self).__init__()
        self.logo_url = logo_url
        self.ico_url = ico_url
        self.main_page_url = main_page_url


class Speaker(object):

    def __init__(self):
        super(Speaker, self).__init__()


class Session(object):

    def __init__(self):
        super(Session, self).__init__()

class Sponsor(object):

    def __init__(self):
        super(Sponsor, self).__init__()


class Microlocation(object):

    def __init__(self):
        super(Microlocation, self).__init__()
