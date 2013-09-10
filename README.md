WTCrud
======

WTCrud is a helper to make the task of doing CRUD (Create, Read, Update, Delete) views easier for those really common tasks like admin interfaces and the like.

WTCrud is designed for applications using what we refer to as WWJS: WTForms, Werkzeug, Jinja2, SQLAlchemy (or alternately flask instead of Werkzeug). What it does is generate a usable UI that can work along with your existing views, login, base templates, etc. All components of WTCrud are designed to be swapped out and extended so that you aren't fighting it, it lets you create elegant interfaces without the rather limiting borg-standard setups.

What WTCrud isn't:
  * A full-fledged admin interface ie Django Admin.
  * A generic provider for CRUD interfaces (right now, SQLAlchemy only)

Goals of WTCrud:
  * Extensible design via subclassing
  * Every piece can be customized or swapped out
  * Support Python2.7 and Python3.3 in the same codebase.