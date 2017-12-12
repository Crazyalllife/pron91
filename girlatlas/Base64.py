#!/usr/bin/env python3
from mimetypes import guess_extension
from urllib.request import urlretrieve

# example image from http://tools.ietf.org/html/rfc2397
url = """data:image/gif;base64,R0lGODdhMAAwAPAAAAAAAP///ywAAAAAMAAw
   AAAC8IyPqcvt3wCcDkiLc7C0qwyGHhSWpjQu5yqmCYsapyuvUUlvONmOZtfzgFz
   ByTB10QgxOR0TqBQejhRNzOfkVJ+5YiUqrXF5Y5lKh/DeuNcP5yLWGsEbtLiOSp
   a/TPg7JpJHxyendzWTBfX0cxOnKPjgBzi4diinWGdkF8kjdfnycQZXZeYGejmJl
   ZeGl9i2icVqaNVailT6F5iJ90m6mvuTS4OK05M0vDk0Q4XUtwvKOzrcd3iq9uis
   F81M1OIcR7lEewwcLp7tuNNkM3uNna3F2JQFo97Vriy/Xl4/f1cf5VWzXyym7PH
   hhx4dbgYKAAA7"""
# filename, m = urlretrieve(url)
#
#
# print(filename, guess_extension(m.get_content_type()))

urls = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAA5JREFUeNpi/M/AABBgAAMFAQGmKnTsAAAAAElFTkSuQmCC'
filename, m = urlretrieve(urls)
print(filename, guess_extension(m.get_content_type()))
