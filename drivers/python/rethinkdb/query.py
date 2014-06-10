from .ast import *
from . import ql2_pb2 as p
import datetime

"""
All top level functions defined here are the starting points for RQL queries
"""
def json(*args):
    return Json(*args)

def js(*args, **kwargs):
    kwargs.setdefault('timeout', ())
    return JavaScript(*args, **kwargs)

def args(*args):
    return Args(*args)

def http(url, **kwargs):
    return Http(func_wrap(url), **kwargs)

def error(*msg):
    return UserError(*msg)

def random(*args, **kwargs):
    return Random(*args, **kwargs)

def do(*args):
    return FunCall(*args)

row = ImplicitVar()

def table(*args, **kwargs):
    kwargs.setdefault('use_outdated', ())
    return Table(*args, **kwargs)

def db(*args):
    return DB(*args)

def db_create(*args):
    return DbCreate(*args)

def db_drop(*args):
    return DbDrop(*args)

def db_list(*args):
    return DbList(*args)

def table_create(*args, **kwargs):
    kwargs.setdefault('primary_key', ())
    kwargs.setdefault('datacenter', ())
    kwargs.setdefault('durability', ())
    return TableCreateTL(*args, **kwargs)

def table_drop(*args):
    return TableDropTL(*args)

def table_list(*args):
    return TableListTL(*args)

def branch(*args):
    return Branch(*args)

# orderBy orders

def asc(*args):
    return Asc(*[func_wrap(arg) for arg in args])

def desc(*args):
    return Desc(*[func_wrap(arg) for arg in args])

# math and logic

def eq(*args):
    return Eq(*args)

def ne(*args):
    return Ne(*args)

def lt(*args):
    return Lt(*args)

def le(*args):
    return Le(*args)

def gt(*args):
    return Gt(*args)

def ge(*args):
    return Ge(*args)

def add(*args):
    return Add(*args)

def sub(*args):
    return Sub(*args)

def mul(*args):
    return Mul(*args)

def div(*args):
    return Div(*args)

def mod(*args):
    return Mod(*args)

def not_(*args):
    return Not(*args)

def and_(*args):
    return All(*args)

def or_(*args):
    return Any(*args)

def all(*args):
    return All(*args)

def any(*args):
    return Any(*args)

def type_of(*args):
    return TypeOf(*args)

def info(*args):
    return Info(*args)

def time(*args):
    return Time(*args)

def iso8601(*args, **kwargs):
    kwargs.setdefault('default_timezone', ())
    return ISO8601(*args, **kwargs)

def epoch_time(*args):
    return EpochTime(*args)

def now(*args):
    return Now(*args)

class RqlTimeName(RqlQuery):
    def compose(self, args, optargs):
        return 'r.'+self.st

# Time enum values
monday      = type('', (RqlTimeName,), {'tt':p.Term.TermType.MONDAY, 'st': 'monday'})()
tuesday     = type('', (RqlTimeName,), {'tt':p.Term.TermType.TUESDAY, 'st': 'tuesday'})()
wednesday   = type('', (RqlTimeName,), {'tt':p.Term.TermType.WEDNESDAY, 'st': 'wednesday'})()
thursday    = type('', (RqlTimeName,), {'tt':p.Term.TermType.THURSDAY, 'st': 'thursday'})()
friday      = type('', (RqlTimeName,), {'tt':p.Term.TermType.FRIDAY, 'st': 'friday'})()
saturday    = type('', (RqlTimeName,), {'tt':p.Term.TermType.SATURDAY, 'st': 'saturday'})()
sunday      = type('', (RqlTimeName,), {'tt':p.Term.TermType.SUNDAY, 'st': 'sunday'})()

january     = type('', (RqlTimeName,), {'tt':p.Term.TermType.JANUARY, 'st': 'january'})()
february    = type('', (RqlTimeName,), {'tt':p.Term.TermType.FEBRUARY, 'st': 'february'})()
march       = type('', (RqlTimeName,), {'tt': p.Term.TermType.MARCH, 'st': 'march'})()
april       = type('', (RqlTimeName,), {'tt': p.Term.TermType.APRIL, 'st': 'april'})()
may         = type('', (RqlTimeName,), {'tt': p.Term.TermType.MAY, 'st': 'may'})()
june        = type('', (RqlTimeName,), {'tt': p.Term.TermType.JUNE, 'st': 'june'})()
july        = type('', (RqlTimeName,), {'tt': p.Term.TermType.JULY, 'st': 'july'})()
august      = type('', (RqlTimeName,), {'tt': p.Term.TermType.AUGUST, 'st': 'august'})()
september   = type('', (RqlTimeName,), {'tt': p.Term.TermType.SEPTEMBER, 'st': 'september'})()
october     = type('', (RqlTimeName,), {'tt': p.Term.TermType.OCTOBER, 'st': 'october'})()
november    = type('', (RqlTimeName,), {'tt': p.Term.TermType.NOVEMBER, 'st': 'november'})()
december    = type('', (RqlTimeName,), {'tt': p.Term.TermType.DECEMBER, 'st': 'december'})()

def make_timezone(*args):
    return RqlTzinfo(*args)

# Merge values
def literal(*args):
    return Literal(*args)

def object(*args):
    return Object(*args)
