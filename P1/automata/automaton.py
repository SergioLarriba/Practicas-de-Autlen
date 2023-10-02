"""Automaton implementation."""

class State():
    """
    Definition of an automaton state. 

    Args:
        name: Name of the state.
        is_final: Whether the state is a final state or not.

    """

    def __init__(self, name, is_final = False):
        self.name = name
        self.is_final = is_final

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.name == other.name and self.is_final == other.is_final

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, is_final={self.is_final!r})"

    def __hash__(self):
        return hash(self.name)


class Transitions(dict):
    """
    Definition of all transitions in an automaton.
    Dictionary of initial states, where each state has a dictionary
    with the final states and the transition symbols. 


    Args:
        transitions: dictionary with a states as keys and dictionary of 
        symbol, final state as key, value tuple. 
        Example:
        {
            q1: {'a': {q2, q1}, 'lambda':{q3}}
            q2: {'a': {q3}, }
            q3: {'lambda':{q1}, 'b':{q2}}
        }

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.transitions == other.transitions

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"{[f'{key}:{self[key]}' for key in self.keys()]})"
        )
        
   
    def add_transition(self, start_state, symbol, end_state):
        """
            Checks that the transition or symbol is not in use and 
            adds one

            Args:
                state: initial state of the transition
                symbol: symbol of the transition
                end_state: final state of the transition
            Returns:
                None
        """

        if self.has_transition_to(start_state, symbol, end_state):
            raise ValueError("Repeated transition or symbol for state '%s'"%start_state)
        
        if self.has_transition(start_state, symbol):
            self[start_state][symbol].add(end_state)
        elif start_state in self.keys():
            self[start_state][symbol] = {end_state}
        else:
            self[start_state] = {symbol: {end_state}}

    """
    for clave, subdiccionario in mi_diccionario.items():
    print(f'Clave exterior: {clave}')
    for subclave, valor in subdiccionario.items():
        print(f'Subclave: {subclave}, Valor: {valor}')
    """
            
    def add_transitions(self, transitions):
        """
            Add transitions from a list

            Args:
                transitions: list of transitions (start, symbol, end)
            Returns:
                None
        """
        for (start_state, symbol, end_state) in transitions:
            self.add_transition(start_state, symbol, end_state)
    
    def has_transition(self, start_state, symbol):
        """
            Checks if a transition defined by a start_state and a symbol is
            contained in Transitions.
        """
        if start_state not in self.__dict__.keys(): 
            return False 
        
        if symbol not in self.__dict__.get(start_state).keys():
            return False
        
        return True 
        

        
    def has_transition_to(self, start_state, symbol, end_state):
        """
            Checks if a transition defined by a start_state, symbol and end_state
            is contained in Transitions.

            Args:
                state: initial state of the transition
                symbol: symbol of the transition
                end_state: final state of the transition
            Returns:
                True/False
        """

        if self is None or start_state is None or end_state is None:
            return False


        transiciones = self.get_all_transitions()
        for transicion in transiciones:
            estado_inicial, simbolo, estado_destino = transicion 
            if estado_inicial == start_state and simbolo==symbol and estado_destino == end_state :
                return True 
            
        return False


    def get_transition(self, state, symbol):
        """
            Returns the corresponding set of states of a initial state and a symbol
            if Transitions has such transition. 

            Args:
                state: initial state of the transition
                symbol: symbol of the transition
            Returns:
                set of states
        """
        # si el estado-simbolo no esta en el diccionario de transiciones 
        if state not in self.__dict__.keys():
            return None 
        estados_finales = set()
        #Si no hay transicion para ese valor en el estado dado
        for estadoInicial, _ in self.__dict__.items():
            if estadoInicial == state and symbol in self.__dict__.get(state):
                estados_finales.update(self.__dict__.get(state).get(symbol))
        return estados_finales
    
    def get_all_transitions(self):
        """
            Returns all transitions in a list.

            Returns:
                list of triplets of transitions
        """

        all_transitions = []

        for start_state in self.keys():
            for symbol in self[start_state]:
                for end_state in self[start_state][symbol]:
                    all_transitions.append((start_state, symbol, end_state))
        
        return all_transitions
        
    

class FiniteAutomaton():
    """Automaton.
    Definiition of a Finite Automaton

    Args:
        initial_state: The initial state of the automaton.
        states: List of states (List[State]) of the automaton. It is converted to a
            tuple internally.
        symbols: List of symbols (List[str]) of the automaton. It is converted to a
            tuple internally.
        transitions: Transitions (Transition) from automaton.

    """

    def __init__(
        self,
        initial_state, states, symbols, transitions,
    ):

        if initial_state not in states:
            raise ValueError(
                f"Initial state {initial_state.name} "
                f"is not in the set of states",
            )

        """
        Check that there are no states with the same name.
        """
        if len(set(states)) != len(states):
            raise ValueError("There are repeated states")

        """
        Check that there are no repeated symbols.
        """
        if len(set(symbols)) != len(symbols):
            raise ValueError("There are repeated symbols")

        self.initial_state = initial_state
        self.states = states
        self.symbols = symbols
        self.transitions = Transitions(transitions)
        

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        # We use sets as the order should not matter
        return (
            self.initial_state == other.initial_state
            and set(self.states) == set(other.states)
            and set(self.symbols) == set(other.symbols)
            and set(self.transitions) == set(other.transitions)
        )

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"initial_state={self.initial_state!r}, "
            f"states={self.states!r}, "
            f"symbols={self.symbols!r}, "
            f"transitions={self.transitions!r})"
        )

    def add_transition(self, start_state, symbol, end_state):
        self.transitions.add_transition(start_state, symbol, end_state)
        
    def add_transitions(self, transitions):
        self.transitions.add_transitions(transitions)

    def has_transition(self, state, symbol):
        return self.transitions.has_transition(state, symbol)
        
    def get_transition(self, state, symbol):
        return self.transitions.get_transition(state, symbol)
        
    def get_all_transitions(self):
        return self.transitions.get_all_transitions()
        
    def to_deterministic(self):
        from automata.dfa import DeterministicFiniteAutomaton
        return DeterministicFiniteAutomaton.to_deterministic(self)
    
    """
    Un automata tiene: estado inicial, final, transicion
    Automaton: tiene una lista de estados [s0, s1, s2] y un objeto: transitions
    Comparar estados -> s0 == s1 
    Transiciones:
        objeto que hereda de dict -> es un diccionario 
        cuando hago aut(aut es un objeto de automaton).transitions[s0]
        las claves del diccionario son estados, para cada estado hay otro diccionario que recoge simbolos y un set de estados finales 
        {s0:{a':{s1, s2}}} -> {key:value}
    
    Clase automatonEvaluator: 
        contiene un automata 
        procesar un simbolo -> cuando viene un simbolo
        aut.hashtransition 
        evaluator -> si una cadena acepta a una automata (llamar a la funcion accept)
        process_symbol -> ej: s0 = q0, si llega lambda vamos a q3, q4, q1 -> mi conjunto de estados es {q0, q3, q4, q1}
        si tengo a -> {q1, q2} -> si hubiese alguna transicion lambda, tengo que añadir tambien las lambda 
    para el primer ej usar el test evaluator -> ver si para una cadena acepta el automata 

    """