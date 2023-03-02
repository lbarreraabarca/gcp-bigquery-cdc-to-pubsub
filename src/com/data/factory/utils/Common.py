
class Common():
    def replace_last_occurrence(self,
                                value: str,
                                old: str,
                                new: str,
                                occurrence: int) -> str:
        value_splitted = value.rsplit(old, occurrence)
        return new.join(value_splitted)

    def replace_first_occurrence(self,
                                 value: str,
                                 old: str,
                                 new: str) -> str:
        value_splitted = value.lstrip(old)
        return new.join(value_splitted)

    def cast(self, value: str, type: str):
        if type == "STRING" or type == "TIMESTAMP":
            return str(value.replace("'", "").replace('"', ''))
        if type == "INTEGER":
            return int(value)
        return None
