import sqlite3


class ORM:
    dbpath = ""
    tablename = ""
    fields = []

    def __init__(self, *kwargs):
        raise NotImplementedError  # prevents making an instance of ORM

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            fields = ", ".join(self.fields)
            qmarks = ", ".join(['?' for _ in self.fields])
            SQL = """ INSERT INTO {} ({}) VALUES ({})""".format(self.tablename, fields, qmarks)
            values = [getattr(self, field) for field in self.fields]
            # [self.field for field in self.fields]
            curs.execute(SQL, values)
            pk = curs.lastrowid
            self.pk = pk

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            set1 = ", ".join(["{}=?".format(field) for field in self.fields])
            SQL = """UPDATE {} SET {} WHERE pk=?""".format(self.tablename, set1)
            values = [getattr(self, field) for field in self.fields] + [self.pk]
            curs.execute(SQL, values)

    def delete(self):  
        if not self.pk:
            raise KeyError(self.__repr__() + " is not a row in " + self.tablename)
        
        with sqlite3.connect(self.dbpath) as conn:   
            curs = conn.cursor()
            SQL = """ DELETE FROM {} WHERE pk=?;""".format(self.tablename)
            curs.execute(SQL, (self.pk,))


    @classmethod
    def one_from_where_clause(cls, where_clause = "", values=tuple()):    
        SQL = "SELECT * FROM {} {};".format(cls.tablename, where_clause)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row      # think of row_factory like DictReader
            curs = conn.cursor()
            curs.execute(SQL, values)
            row = curs.fetchone()
            if not row:
                return None
            return cls(**row)                     


    @classmethod
    def all_from_where_clause(cls, where_clause='', values=tuple()):
        SQL = "SELECT * FROM {} {};".format(cls.tablename, where_clause)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            curs.execute(SQL, values)
            rows = curs.fetchall()
            return [cls(**row) for row in rows]        



    @classmethod
    def one_from_pk(cls,pk):
        return cls.one_from_where_clause("WHERE pk=?", (pk,))

    def __repr__(self):
        return "< {} ORM: pk={} >".format(self.tablename, self.pk)


