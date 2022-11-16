from ArbolesRojinegros import ArbolRojinegro


class RojinegroGenerador:

    def ejemplo1(self):
        ejemplo = ArbolRojinegro(
                ArbolRojinegro(
                        None,
                        None,
                        1,
                        True
                ),
                ArbolRojinegro(
                        ArbolRojinegro(
                                None,
                                None,
                                3,
                                True
                        ),
                        ArbolRojinegro(
                                None,
                                None,
                                5,
                                True
                        ),
                        4,
                        False
                ),
                2,
                True
        )
        return ejemplo

    def ejemplo2(self):
        ejemplo =  ArbolRojinegro(
                 ArbolRojinegro(
                        None,
                        None,
                        1,
                        True
                ),
                 ArbolRojinegro(
                         ArbolRojinegro(
                                None,
                                None,
                                6,
                                True
                        ),
                         ArbolRojinegro(
                                None,
                                None,
                                9,
                                True
                        ),
                        8,
                        False
                ),
                5,
                True
        )
        return ejemplo


    def ejemplo3(self):
        ejemplo =  ArbolRojinegro(

                 ArbolRojinegro(
                         ArbolRojinegro(
                                None,
                                None,
                                1,
                                True
                        ),
                         ArbolRojinegro(
                                None,
                                None,
                                3,
                                True
                        ),
                        2,
                        False
                ),
                 ArbolRojinegro(
                        None,
                        None,
                        5,
                        True
                ),
                4,
                True
        )
        return ejemplo;

    def ejemplo4(self):
        ejemplo =  ArbolRojinegro(

                 ArbolRojinegro(
                         ArbolRojinegro(
                                None,
                                None,
                                1,
                                True
                        ),
                         ArbolRojinegro(
                                None,
                                None,
                                6,
                                True
                        ),
                        5,
                        False
                ),
                 ArbolRojinegro(
                        None,
                        None,
                        9,
                        True
                ),
                8,
                True
        )
        return ejemplo
