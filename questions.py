# Complete 50-Question Bank compiled from Modules 1, 2, and 3 PDFs

QUESTION_BANK = [
    # --- MODULE 1 (Questions 1 - 10) ---
    {
        "id": 1,
        "module": "Module 1",
        "topic": "PEAS & Environment Classification",
        "type": "Scenario-Based",
        "question": "An autonomous high-frequency algorithmic trading agent operates in the global foreign exchange (Forex) market. It analyzes live price streams, news feeds, and competitor order books to execute high-volume currency trades in milliseconds. Under the PEAS framework, how is this task environment categorized?",
        "options": [
            "Fully Observable, Deterministic, Episodic, Static, Discrete, Single-Agent",
            "Partially Observable, Stochastic, Sequential, Dynamic, Continuous, Multi-Agent",
            "Partially Observable, Deterministic, Sequential, Static, Continuous, Multi-Agent",
            "Fully Observable, Stochastic, Episodic, Dynamic, Discrete, Single-Agent"
        ],
        "answer": "Partially Observable, Stochastic, Sequential, Dynamic, Continuous, Multi-Agent",
        "hint": "Consider whether the trading bot can see private internal strategies of rival traders and whether prices change while decisions are made.",
        "explanation": "Partially Observable (cannot see rival algorithms), Stochastic (market shocks), Sequential (trades alter future capital), Dynamic (prices change during computation), Continuous (prices/time metrics), Multi-Agent (competes with other traders)."
    },
    {
        "id": 2,
        "module": "Module 1",
        "topic": "Rationality vs. Omniscience",
        "type": "Assertion-Reason",
        "question": "Assertion (A): An automated self-driving car that executes a legal turn at a clear intersection and is subsequently struck by an unexpected falling meteoroid cannot be classified as 'irrational'.\nReason (R): Rationality evaluates the expected utility of an action based on the percept sequence to date and prior knowledge, whereas perfection (omniscience) evaluates the actual outcome after the fact.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "answer": "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
        "hint": "Distinguish between a decision made using sound logic and evidence versus an outcome known only in hindsight.",
        "explanation": "Rationality depends on evidence gathered up to decision time. An agent cannot be judged irrational for unobservable, low-probability events. Rationality maximizes expected performance, not actual outcome."
    },
    {
        "id": 3,
        "module": "Module 1",
        "topic": "Graph Search vs. Tree Search Node Expansion",
        "type": "Problem-Solving / Numerical",
        "question": "Consider an agent navigating an infinite 2D rectangular grid without obstacles starting at state (0,0) (step cost = 1). If search depth limit is d = 2:\n1. How many total leaf nodes exist in a Tree Search?\n2. How many total distinct states are stored in Graph Search (explored + frontier)?",
        "options": [
            "Tree Search Leaves = 16 | Graph Search States = 13",
            "Tree Search Leaves = 16 | Graph Search States = 9",
            "Tree Search Leaves = 12 | Graph Search States = 13",
            "Tree Search Leaves = 8 | Graph Search States = 5"
        ],
        "answer": "Tree Search Leaves = 16 | Graph Search States = 13",
        "hint": "For Tree Search, calculate b^d where b=4. For Graph Search, count unique coordinates (x,y) with |x|+|y| <= 2.",
        "explanation": "Tree Search: Leaves at d=2 equal 4^2 = 16. Graph Search: Distance 0 (1 state) + Distance 1 (4 states) + Distance 2 (8 states) = 13 distinct states."
    },
    {
        "id": 4,
        "module": "Module 1",
        "topic": "Problem Characteristics",
        "type": "Match the Following",
        "question": "Match each AI problem domain with its primary characteristic:\n1. Symbolic Integration (∫(x² + sin x)dx) -> Q. Decomposable\n2. Mathematical Theorem Proving -> R. Ignorable Steps\n3. Playing a Game of Chess -> S. Recoverable Steps\n4. Performing Robotic Eye Surgery -> P. Irrecoverable Steps",
        "options": [
            "1-Q, 2-R, 3-S, 4-P",
            "1-R, 2-Q, 3-P, 4-S",
            "1-Q, 2-P, 3-S, 4-R",
            "1-S, 2-R, 3-Q, 4-P"
        ],
        "answer": "1-Q, 2-R, 3-S, 4-P",
        "hint": "Determine whether failed steps can be ignored, undone through counter-actions, or cannot be undone at all.",
        "explanation": "Integration decomposes into subproblems; Theorem proving steps can be ignored if unhelpful; Chess errors are recoverable via moves; Eye surgery mistakes are physically irrecoverable."
    },
    {
        "id": 5,
        "module": "Module 1",
        "topic": "Local Search Anomalies",
        "type": "Fill in the Blanks",
        "question": "In local search optimization, a _____ is a flat area of state-space where adjacent states have identical evaluation values, whereas a _____ is an elevated area with a sequence of local maxima not directly connected by single axis-aligned steps.",
        "options": [
            "Plateau / Ridge",
            "Ridge / Local Maximum",
            "Shoulder / Foothill",
            "Valley / Plateau"
        ],
        "answer": "Plateau / Ridge",
        "hint": "One feature is flat with zero gradient; the other is a steep narrow crest sloping diagonally.",
        "explanation": "A Plateau is flat with constant heuristic values. A Ridge is a sequence of local maxima oriented diagonally to grid moves, causing search oscillations."
    },
    {
        "id": 6,
        "module": "Module 1",
        "topic": "CSP & Arc Consistency",
        "type": "Scenario / Application",
        "question": "Exam timetabling CSP: Variable A domain = {Slot 1, Slot 2}, Variable B domain = {Slot 1}. Constraint: A ≠ B. If AC-3 enforces consistency on directed arc (A, B), what is the updated domain of A?",
        "options": [
            "{Slot 1, Slot 2}",
            "{Slot 1}",
            "{Slot 2}",
            "(Empty Domain)"
        ],
        "answer": "{Slot 2}",
        "hint": "Arc consistency removes values from Domain(A) that have no valid non-conflicting match in Domain(B).",
        "explanation": "If A=Slot 1, B can only be Slot 1 (violates A≠B), so Slot 1 is removed. If A=Slot 2, B=Slot 1 satisfies constraint. Thus, Domain(A) = {Slot 2}."
    },
    {
        "id": 7,
        "module": "Module 1",
        "topic": "Uninformed Search Complexities",
        "type": "True/False",
        "question": "True or False: Iterative Deepening Search (IDS) re-expands shallow nodes multiple times, causing its asymptotic time complexity on a uniform tree (b > 1, depth d) to be significantly higher than BFS.",
        "options": ["True", "False"],
        "answer": "False",
        "hint": "Express total node expansions algebraically: majority of nodes lie at the bottom depth d.",
        "explanation": "False. Total expansions in IDS = O(b^d), matching BFS. Re-expansion overhead is minimal because bottom-level leaf nodes dominate the total count."
    },
    {
        "id": 8,
        "module": "Module 1",
        "topic": "Means-End Analysis Strategy",
        "type": "MCQ",
        "question": "Which core strategy differentiates Means-End Analysis (GPS) from standard uninformed forward search?",
        "options": [
            "It expands states in order of increasing cumulative path cost g(n).",
            "It detects the primary difference between current state and goal state, selects an operator to reduce that difference, and creates subgoals if preconditions are not met.",
            "It converts state variables into Boolean clauses and applies resolution refutation.",
            "It performs continuous gradient ascent along the steepest slope of h(n)."
        ],
        "answer": "It detects the primary difference between current state and goal state, selects an operator to reduce that difference, and creates subgoals if preconditions are not met.",
        "hint": "Think about difference reduction and recursive subgoal generation.",
        "explanation": "Means-End Analysis centers on difference reduction between current state and goal, selecting specific difference-reducing operators and generating subgoals."
    },
    {
        "id": 9,
        "module": "Module 1",
        "topic": "Uniform-Cost Search Behavior",
        "type": "Scenario / Problem Solving",
        "question": "In Uniform-Cost Search (UCS), why is it mandatory to apply the goal test to a node only when it is popped from the priority queue (expanded) rather than when generated?",
        "options": [
            "To prevent the search queue from exceeding memory limits.",
            "Because generating a child node does not guarantee that the path found to it is the minimum-cost path; a cheaper path to that goal may still exist in the frontier.",
            "Because goal testing during generation creates infinite loops.",
            "To ensure the algorithm behaves like Depth-First Search."
        ],
        "answer": "Because generating a child node does not guarantee that the path found to it is the minimum-cost path; a cheaper path to that goal may still exist in the frontier.",
        "hint": "A goal node generated early might arrive via an expensive edge, while a cheaper multi-step path remains in the queue.",
        "explanation": "Popping a node guarantees no remaining path in the queue has a lower cost. Testing at generation risks accepting an optimal node reached via a suboptimal path."
    },
    {
        "id": 10,
        "module": "Module 1",
        "topic": "Production Systems Architecture",
        "type": "Conceptual MCQ",
        "question": "In a rule-based Production System, what specific mechanism executes when multiple rules simultaneously have their IF-conditions satisfied by Working Memory?",
        "options": [
            "Backtracking Strategy",
            "Conflict Resolution Strategy",
            "State-Space Pruning",
            "Pattern Matching Engine"
        ],
        "answer": "Conflict Resolution Strategy",
        "hint": "When multiple rules match, a selection policy is needed to pick which rule fires.",
        "explanation": "The Conflict Resolution Strategy selects which rule fires from the conflict set using criteria like specificity, recency, or rule priority."
    },

    # --- MODULE 2 (Questions 11 - 30) ---
    {
        "id": 11,
        "module": "Module 2",
        "topic": "Search Space Complexity",
        "type": "Problem-Solving / Numerical",
        "question": "Tree search with uniform branching b=5, max depth m=10, shallowest goal depth d=4. Comparing DFS (limit m) against BFS:\n1. Max nodes stored in memory by DFS?\n2. Max nodes stored in memory by BFS at goal depth d?",
        "options": [
            "DFS: 50 nodes | BFS: 625 nodes",
            "DFS: 50 nodes | BFS: 10 nodes",
            "DFS: 9.7 × 10^6 nodes | BFS: 625 nodes",
            "DFS: 15 nodes | BFS: 20 nodes"
        ],
        "answer": "DFS: 50 nodes | BFS: 625 nodes",
        "hint": "DFS memory complexity is O(b*m), while BFS memory complexity is dominated by O(b^d).",
        "explanation": "DFS memory = b * m = 5 * 10 = 50 nodes. BFS memory at goal depth = b^d = 5^4 = 625 nodes."
    },
    {
        "id": 12,
        "module": "Module 2",
        "topic": "PEAS Framework for Medical Systems",
        "type": "Scenario / Application",
        "question": "For an AI clinical decision support system (softbot) evaluating patient symptoms to suggest diagnoses and treatments, identify the correct Sensors and Actuators:",
        "options": [
            "Sensors: Keyboard/EHR data entry of symptoms and findings | Actuators: Display screen showing diagnoses, test suggestions, and treatment plans",
            "Sensors: Cameras and blood pressure monitors | Actuators: Robotic surgical arms and automated pumps",
            "Sensors: Display screen showing diagnoses | Actuators: Keyboard entries made by doctors",
            "Sensors: Downlink satellite feeds | Actuators: Valves, heaters, and physical pumps"
        ],
        "answer": "Sensors: Keyboard/EHR data entry of symptoms and findings | Actuators: Display screen showing diagnoses, test suggestions, and treatment plans",
        "hint": "Focus on how a software agent inputs and displays information to clinicians.",
        "explanation": "Sensors are electronic health record inputs and keyboard data entry. Actuators are screen displays showing diagnostic predictions and therapeutic suggestions."
    },
    {
        "id": 13,
        "module": "Module 2",
        "topic": "Admissibility vs. Consistency in A* Search",
        "type": "Assertion-Reason",
        "question": "Assertion (A): In Graph Search, an admissible heuristic h(n) alone is always sufficient to guarantee that A* finds the optimal path without needing to re-open nodes in the explored set.\nReason (R): A heuristic h(n) is consistent if h(n) ≤ c(n,a,n') + h(n'), ensuring f(n) = g(n)+h(n) is non-decreasing.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "answer": "(A) is false, but (R) is true.",
        "hint": "Admissibility guarantees optimality for Tree Search; Graph Search requires Consistency to avoid reopening nodes.",
        "explanation": "Assertion (A) is False: Graph Search requires heuristic Consistency (monotonicity), not just Admissibility, to prevent reopening closed nodes. Reason (R) is True: defines consistency."
    },
    {
        "id": 14,
        "module": "Module 2",
        "topic": "Hill Climbing Variants",
        "type": "MCQ",
        "question": "Which specific variation of Hill Climbing generates successors randomly one by one and immediately selects the first successor that improves upon the current state?",
        "options": [
            "Steepest-Ascent Hill Climbing",
            "First-Choice Hill Climbing",
            "Stochastic Hill Climbing",
            "Random-Restart Hill Climbing"
        ],
        "answer": "First-Choice Hill Climbing",
        "hint": "Evaluates generated neighbors one by one and picks the first improving move.",
        "explanation": "First-Choice Hill Climbing selects the first generated neighbor that yields an improvement, making it ideal when nodes have vast successor states."
    },
    {
        "id": 15,
        "module": "Module 2",
        "topic": "Uninformed Search & Frontier Structures",
        "type": "Match the Following",
        "question": "Match each search algorithm with its frontier data structure:\n1. BFS -> Q. FIFO Queue\n2. DFS -> S. LIFO Queue (Stack)\n3. UCS -> P. Priority Queue ordered by path cost g(n)\n4. Greedy Best-First -> R. Priority Queue ordered by heuristic h(n)",
        "options": [
            "1-Q, 2-S, 3-P, 4-R",
            "1-S, 2-Q, 3-R, 4-P",
            "1-Q, 2-P, 3-S, 4-R",
            "1-P, 2-S, 3-Q, 4-R"
        ],
        "answer": "1-Q, 2-S, 3-P, 4-R",
        "hint": "Connect BFS to FIFO, DFS to Stack, UCS to cumulative cost g(n), and Greedy to heuristic h(n).",
        "explanation": "BFS uses FIFO queue; DFS uses LIFO stack; UCS uses Priority Queue by g(n); Greedy Best-First uses Priority Queue by h(n)."
    },
    {
        "id": 16,
        "module": "Module 2",
        "topic": "Greedy Best-First Search Properties",
        "type": "True/False",
        "question": "True or False: Greedy Best-First Search uses f(n) = h(n). Because it expands nodes closest to goal, it is guaranteed to be complete and optimal in general graphs.",
        "options": ["True", "False"],
        "answer": "False",
        "hint": "Does Greedy search consider accrued path cost g(n)? Can it enter infinite loops?",
        "explanation": "False. Greedy Best-First Search ignores accrued cost g(n), making it non-optimal. It is also incomplete as it can get stuck in infinite loops."
    },
    {
        "id": 17,
        "module": "Module 2",
        "topic": "CSP Heuristics Selection",
        "type": "Scenario / Problem Solving",
        "question": "Map coloring CSP with domains: Domain(V2)={G,B} (size 2), Domain(V3)={B} (size 1), Domain(V4)={G,B} (size 2), Domain(V5)={B} (size 1). Constraints: V3 linked to 2 unassigned vars, V5 linked to 3 unassigned vars. Applying MRV tie-broken by Degree Heuristic selects:",
        "options": ["V2", "V3", "V4", "V5"],
        "answer": "V5",
        "hint": "MRV picks smallest domain size (V3 & V5 tie with 1). Degree heuristic breaks ties by most constraints on unassigned vars.",
        "explanation": "MRV filters to V3 and V5 (domain size 1). Degree heuristic breaks tie: Degree(V3)=2, Degree(V5)=3. Thus V5 is selected."
    },
    {
        "id": 18,
        "module": "Module 2",
        "topic": "Agent Function vs. Agent Program",
        "type": "Fill in the Blanks",
        "question": "An abstract mathematical mapping from a complete _____ to an action is the agent function, whereas a concrete physical implementation taking only the current _____ is the agent program.",
        "options": [
            "percept sequence / percept",
            "state space / heuristic",
            "condition-action rule / environment",
            "performance measure / goal"
        ],
        "answer": "percept sequence / percept",
        "hint": "One considers full history; the other receives current instantaneous sensor input.",
        "explanation": "Agent function maps full percept sequence history to actions. Agent program runs on physical architecture taking only current single percept."
    },
    {
        "id": 19,
        "module": "Module 2",
        "topic": "8-Puzzle Heuristic Calculation",
        "type": "Problem-Solving / Numerical",
        "question": "Current: [[1,2,3],[4,8,5],[6,7,-]], Goal: [[1,2,3],[4,5,6],[7,8,-]]. Calculate:\n1. h1: Misplaced tiles (excl. blank)\n2. h2: Sum of Manhattan distances",
        "options": [
            "h1 = 4 and h2 = 6",
            "h1 = 3 and h2 = 4",
            "h1 = 4 and h2 = 8",
            "h1 = 5 and h2 = 6"
        ],
        "answer": "h1 = 4 and h2 = 6",
        "hint": "Count misplaced numbered tiles (5,8,6,7). Sum horizontal + vertical tile shifts to goal positions.",
        "explanation": "Misplaced tiles = 4 (tiles 5,8,6,7). Manhattan distances: Tile 5 (1 step) + Tile 6 (3 steps) + Tile 7 (1 step) + Tile 8 (1 step) = 6."
    },
    {
        "id": 20,
        "module": "Module 2",
        "topic": "Loopy Paths vs. Redundant Paths",
        "type": "Conceptual MCQ",
        "question": "What is the key distinction between a loopy path and a general redundant path in search graphs?",
        "options": [
            "A loopy path is a directed cycle returning to a state on current path, whereas a redundant path is any route reaching an already discovered state with equal/higher cost.",
            "Loopy paths occur only in tree search; redundant paths occur only in graph search.",
            "Loopy paths make state spaces infinite; redundant paths make state spaces continuous.",
            "Redundant paths affect space complexity; loopy paths affect heuristic accuracy."
        ],
        "answer": "A loopy path is a directed cycle returning to a state on current path, whereas a redundant path is any route reaching an already discovered state with equal/higher cost.",
        "hint": "A loop returns to a state on the active branch path; redundant paths reach duplicate states via suboptimal routes.",
        "explanation": "Loopy paths form explicit cycles along the active path. Redundant paths include any route that reaches a previously explored state with non-optimal cost."
    },
    {
        "id": 21,
        "module": "Module 2",
        "topic": "Iterative Deepening Search Node Count",
        "type": "Problem-Solving / Numerical",
        "question": "IDS search on uniform tree (b=3, goal depth d=3). Checking goal at each limit l=0 to l=3, what is the exact total number of node expansions across all iterations combined?",
        "options": ["58", "40", "81", "27"],
        "answer": "58",
        "hint": "Sum node expansions at each level k: (d - k + 1) * b^k for k = 0, 1, 2, 3.",
        "explanation": "Level 0: 4*3^0 = 4; Level 1: 3*3^1 = 9; Level 2: 2*3^2 = 18; Level 3: 1*3^3 = 27. Total = 4 + 9 + 18 + 27 = 58 expansions."
    },
    {
        "id": 22,
        "module": "Module 2",
        "topic": "Model-Based Reflex Agents",
        "type": "Scenario-Based",
        "question": "An AGV robot in a warehouse loses Wi-Fi localization signal beneath metal shelves. Why does Simple Reflex Agent fail while Model-Based Reflex Agent continues moving safely?",
        "options": [
            "Simple reflex relies strictly on current percepts and halts when input drops, whereas model-based updates internal state estimates using transition history.",
            "Simple reflex uses h(n) functions requiring A* search, whereas model-based uses simple lookup tables.",
            "Simple reflex requires continuous state spaces, whereas model-based works only in discrete spaces.",
            "Simple reflex cannot move physically without GPS coordinates."
        ],
        "answer": "Simple reflex relies strictly on current percepts and halts when input drops, whereas model-based updates internal state estimates using transition history.",
        "hint": "An internal state allows estimation of world status during transient sensor blackouts.",
        "explanation": "Simple Reflex agents operate strictly on current percepts and fail during blackouts. Model-Based agents track internal state using transition models to estimate positions."
    },
    {
        "id": 23,
        "module": "Module 2",
        "topic": "Heuristic Dominance in A* Search",
        "type": "Assertion-Reason",
        "question": "Assertion (A): If h1(n) and h2(n) are admissible heuristics, then h3(n) = max(h1(n), h2(n)) is admissible and strictly dominates both.\nReason (R): A heuristic hA dominates hB if hA(n) ≥ hB(n) for all n, guaranteeing A* expands fewer or equal nodes.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "answer": "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
        "hint": "Taking the maximum of two underestimating heuristics remains admissible and closer to true cost h*.",
        "explanation": "Max of two admissible heuristics remains ≤ h* (admissible). Higher estimates prune larger search branches, expanding fewer nodes."
    },
    {
        "id": 24,
        "module": "Module 2",
        "topic": "Simulated Annealing Behavior",
        "type": "Fill in the Blanks",
        "question": "In Simulated Annealing, downhill probability P = e^(ΔE/T). As Temperature T -> 0, algorithm behaves as _____; as T -> ∞, it behaves as _____.",
        "options": [
            "Pure Hill Climbing / a Random Walk",
            "a Random Walk / Pure Hill Climbing",
            "First-Choice Hill Climbing / A* Search",
            "Local Beam Search / Genetic Algorithm"
        ],
        "answer": "Pure Hill Climbing / a Random Walk",
        "hint": "Evaluate limit of e^(ΔE/T) when T->0 (prob->0) vs T->∞ (prob->1).",
        "explanation": "As T->0, probability of bad moves drops to 0 (Pure Hill Climbing). As T->∞, probability of bad moves approaches 1 (Random Walk)."
    },
    {
        "id": 25,
        "module": "Module 2",
        "topic": "Uninformed Search Complexity Bounds",
        "type": "Match the Following",
        "question": "Match uninformed algorithms with worst-case bounds:\n1. BFS -> R. Time: O(b^d) | Space: O(b^d)\n2. DFS -> P. Time: O(b^m) | Space: O(b*m)\n3. IDS -> S. Time: O(b^d) | Space: O(b*d)\n4. UCS -> Q. Time: O(b^(1+⌊C*/ε⌋)) | Space: O(b^(1+⌊C*/ε⌋))",
        "options": [
            "1-R, 2-P, 3-S, 4-Q",
            "1-P, 2-R, 3-Q, 4-S",
            "1-S, 2-P, 3-R, 4-Q",
            "1-R, 2-S, 3-P, 4-Q"
        ],
        "answer": "1-R, 2-P, 3-S, 4-Q",
        "hint": "Identify linear space algorithms O(b*d) vs cost-bounded step algorithms.",
        "explanation": "BFS requires O(b^d) space; DFS requires linear depth O(b*m) space; IDS achieves O(b*d) linear space; UCS is bounded by cost C*/ε."
    },
    {
        "id": 26,
        "module": "Module 2",
        "topic": "Forward Checking vs. Arc Consistency",
        "type": "Scenario / Application",
        "question": "Map coloring triangle {A,B,C}, domains {Red, Blue}. Assign A = Red. What happens under Forward Checking vs. AC-3?",
        "options": [
            "Forward Checking prunes B and C domains to {Blue}, failing to detect conflict between B and C; AC-3 detects B≠C is impossible and flags failure immediately.",
            "Both Forward Checking and AC-3 detect failure immediately.",
            "Forward Checking solves problem; AC-3 enters infinite loop.",
            "Neither algorithm prunes any values."
        ],
        "answer": "Forward Checking prunes B and C domains to {Blue}, failing to detect conflict between B and C; AC-3 detects B≠C is impossible and flags failure immediately.",
        "hint": "Forward checking inspects arcs connected to assigned var A. AC-3 propagates across unassigned vars (B,C).",
        "explanation": "Forward Checking leaves Domain(B)={Blue} and Domain(C)={Blue} without checking B≠C. AC-3 checks arc (B,C), finds no valid assignment, and flags failure."
    },
    {
        "id": 27,
        "module": "Module 2",
        "topic": "Philosophical Foundations & Turing Test",
        "type": "Conceptual MCQ",
        "question": "John Searle devised the 'Chinese Room' thought experiment (1980) primarily to refute which foundational assumption?",
        "options": [
            "That passing the Turing Test via syntactic symbol manipulation proves true intentionality, semantics, and conscious mind (refuting Strong AI).",
            "That computers can simulate rational decision-making in financial markets (refuting Weak AI).",
            "That heuristic algorithms can solve NP-complete constraint satisfaction problems.",
            "That neural networks are capable of pattern recognition."
        ],
        "answer": "That passing the Turing Test via syntactic symbol manipulation proves true intentionality, semantics, and conscious mind (refuting Strong AI).",
        "hint": "Focus on Searle's distinction between syntax (manipulating symbols) and semantics (true understanding).",
        "explanation": "The Chinese Room demonstrates that pure syntactic symbol manipulation does not produce semantic understanding or consciousness, refuting Strong AI."
    },
    {
        "id": 28,
        "module": "Module 2",
        "topic": "8-Queens Complete-State Heuristic",
        "type": "Problem-Solving / Numerical",
        "question": "4-Queens configuration: Q1(1,4), Q2(2,2), Q3(3,4), Q4(4,2). Calculate evaluation heuristic h(n) = number of attacking pairs:",
        "options": ["2", "4", "3", "1"],
        "answer": "2",
        "hint": "Check all distinct pairs (Qi, Qj) for horizontal (same row) or diagonal attacks.",
        "explanation": "Horizontal attack pair 1: Q1(1,4) and Q3(3,4) on row 4. Horizontal attack pair 2: Q2(2,2) and Q4(4,2) on row 2. Total attacking pairs = 2."
    },
    {
        "id": 29,
        "module": "Module 2",
        "topic": "Open-Loop vs. Closed-Loop Problem Solving",
        "type": "True/False",
        "question": "True or False: In a partially observable and stochastic environment, an agent can safely execute an open-loop pre-computed action sequence without checking sensors.",
        "options": ["True", "False"],
        "answer": "False",
        "hint": "Open-loop systems ignore sensor percepts. Is this safe when action outcomes are stochastic?",
        "explanation": "False. Open-loop execution ignores percepts and fails in stochastic/partially observable environments. Closed-loop sensing is required to monitor contingencies."
    },
    {
        "id": 30,
        "module": "Module 2",
        "topic": "Means-End Analysis & Goal Reduction",
        "type": "Scenario / Application",
        "question": "Service robot cleaning floor: Goal = Floor dry. Primary operator = DryFloor(Mop) requiring precondition Hold(Mop). Robot currently does NOT hold mop. How does MEA respond?",
        "options": [
            "Aborts execution and declares permanent failure.",
            "Calculates Euclidean distance and runs simulated annealing.",
            "Detects difference between current state and precondition, establishes new subgoal Hold(Mop), and searches for operator UnlockCloset.",
            "Executes random walk movement until stumblng into mop."
        ],
        "answer": "Detects difference between current state and precondition, establishes new subgoal Hold(Mop), and searches for operator UnlockCloset.",
        "hint": "Unsatisfied operator preconditions spark recursive subgoal creation.",
        "explanation": "MEA detects precondition mismatch, creates recursive subgoal Hold(Mop), and selects operators to fulfill preconditions."
    },

    # --- MODULE 3 (Questions 31 - 50) ---
    {
        "id": 31,
        "module": "Module 3",
        "topic": "AC-3 Time Complexity",
        "type": "Problem-Solving / Numerical",
        "question": "CSP with n variables, max domain size d, e binary constraints (edges). What is worst-case asymptotic time complexity of AC-3 arc consistency?",
        "options": [
            "O(e * d^3)",
            "O(n^2 * d^2)",
            "O(e * d^2)",
            "O(n * d^3)"
        ],
        "answer": "O(e * d^3)",
        "hint": "Arc evaluation queue insertions bounded by O(e * d); per-arc consistency check takes O(d^2).",
        "explanation": "Total queue insertions bounded by O(e * d). Per-arc check testing d values against d values takes O(d^2). Total time = O(e * d^3)."
    },
    {
        "id": 32,
        "module": "Module 3",
        "topic": "Consistent Heuristics & Monotonicity",
        "type": "Assertion-Reason",
        "question": "Assertion (A): In A* search with consistent heuristic h(n), sequence of f-values of popped nodes from priority queue is non-decreasing.\nReason (R): Consistent heuristic satisfies h(n) ≤ c(n,a,n') + h(n'), forcing f(n') = g(n') + h(n') ≥ f(n).",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "answer": "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
        "hint": "Substitute g(n') = g(n) + c(n,a,n') into consistency inequality.",
        "explanation": "Consistency h(n) ≤ c + h(n') + g(n) => f(n) ≤ f(n'). Proves f-values are non-decreasing along paths, guaranteeing goal optimality when popped."
    },
    {
        "id": 33,
        "module": "Module 3",
        "topic": "Genetic Algorithm Mechanisms",
        "type": "Scenario / Application",
        "question": "Microchip layout Genetic Algorithm prematurely converges with identical bit values across bits 12-18, losing diversity. Which GA component restores lost genetic diversity?",
        "options": [
            "Mutation",
            "Crossover (Recombination)",
            "Fitness-Proportional Selection",
            "Rank-Based Selection"
        ],
        "answer": "Mutation",
        "hint": "Crossover only recombines existing alleles; if a bit is 0 in all parents, crossover cannot flip it to 1.",
        "explanation": "Mutation randomly flips individual bits, introducing entirely new genetic material to break out of premature local convergence traps."
    },
    {
        "id": 34,
        "module": "Module 3",
        "topic": "Goal-Based vs. Utility-Based Agents",
        "type": "Scenario-Based",
        "question": "Electric vehicle evaluates Route 1 (25m, $10, 5% batt), Route 2 (30m, $0, 30% batt), Route 3 (45m, $0, 60% batt). How do Goal-Based and Utility-Based agents differ?",
        "options": [
            "Goal-Based treats all routes reaching destination as equal binary successes; Utility-Based uses a real-valued function to compute trade-offs between speed, cost, and battery safety.",
            "Goal-Based selects Route 1 using A*; Utility-Based selects Route 3 using DFS.",
            "Goal-Based requires continuous environments; Utility-Based operates strictly in discrete environments.",
            "Goal-Based computes probability distributions; Utility-Based operates deterministically."
        ],
        "answer": "Goal-Based treats all routes reaching destination as equal binary successes; Utility-Based uses a real-valued function to compute trade-offs between speed, cost, and battery safety.",
        "hint": "Goals give binary yes/no assessment; Utility functions calculate continuous trade-offs.",
        "explanation": "Goal agents evaluate binary goal satisfaction. Utility agents calculate continuous trade-offs U(s) across speed, cost, and safety."
    },
    {
        "id": 35,
        "module": "Module 3",
        "topic": "A* Expansion Order",
        "type": "Problem-Solving / Numerical",
        "question": "Graph with h(S)=6, h(A)=4, h(B)=2, h(C)=4, h(G)=0. Edges: S->A (2), S->B (5), A->C (2), B->G (4), C->G (1). Breaking ties alphabetically, what is the A* expansion order?",
        "options": [
            "S -> A -> C -> G",
            "S -> A -> B -> G",
            "S -> B -> A -> C -> G",
            "S -> A -> B -> C -> G"
        ],
        "answer": "S -> A -> B -> C -> G",
        "hint": "Track priority queue by f(n) = g(n) + h(n).",
        "explanation": "Pop S(f=6) -> Frontier [A(f=6), B(f=7)]; Pop A(f=6) -> Frontier [B(f=7), C(f=8)]; Pop B(f=7) -> Frontier [C(f=8), G(f=9)]; Pop C(f=8) updates G to f=5 -> Pop G(f=5)."
    },
    {
        "id": 36,
        "module": "Module 3",
        "topic": "Inference Engine Mechanisms",
        "type": "Match the Following",
        "question": "Match production system reasoning mechanisms:\n1. Forward Chaining -> Q. Data-driven evaluate facts\n2. Backward Chaining -> P. Goal-driven evaluate hypotheses\n3. Rete Algorithm -> S. Directed acyclic graph pattern matching\n4. Recency Strategy -> R. Prioritize newly added working memory facts",
        "options": [
            "1-Q, 2-P, 3-S, 4-R",
            "1-P, 2-Q, 3-R, 4-S",
            "1-Q, 2-S, 3-P, 4-R",
            "1-S, 2-P, 3-Q, 4-R"
        ],
        "answer": "1-Q, 2-P, 3-S, 4-R",
        "hint": "Distinguish data-driven from goal-driven reasoning and graph pattern caching.",
        "explanation": "Forward Chaining starts from facts; Backward Chaining starts from hypotheses; Rete constructs DAG graph matching; Recency prioritizes new facts."
    },
    {
        "id": 37,
        "module": "Module 3",
        "topic": "Intelligent Backtracking in CSPs",
        "type": "Fill in the Blanks",
        "question": "Conflict-Directed Backjumping jumps back directly to the most recent variable in the _____ set, while _____ updates conflict sets dynamically to prevent re-exploring fruitless subtrees.",
        "options": [
            "Conflict / Dynamic Backtracking",
            "Domain / Arc Consistency",
            "Frontier / Forward Checking",
            "Heuristic / Min-Conflicts"
        ],
        "answer": "Conflict / Dynamic Backtracking",
        "hint": "Identify the set tracking variables responsible for domain wipeouts.",
        "explanation": "Conflict-Directed Backjumping jumps back to the conflict set responsible for domain wipeout. Dynamic Backtracking preserves non-conflicting assignments."
    },
    {
        "id": 38,
        "module": "Module 3",
        "topic": "Environment Properties",
        "type": "True/False",
        "question": "True or False: In an episodic task environment, experience is divided into independent episodes where actions in one episode do NOT affect future states of subsequent episodes.",
        "options": ["True", "False"],
        "answer": "True",
        "hint": "Contrast visual conveyor belt defect inspection with playing Chess.",
        "explanation": "True. In episodic environments, each episode is atomic and independent, with no cross-episode state effects."
    },
    {
        "id": 39,
        "module": "Module 3",
        "topic": "Search Design & Edge Costs",
        "type": "Conceptual MCQ",
        "question": "Why is BFS conceptually incapable of guaranteeing shortest paths on real-world maps with road distances ranging from 50 meters to 15 kilometers?",
        "options": [
            "BFS treats all edges as equal step cost (c=1) and optimizes for fewest edge hops, not cumulative distance g(n).",
            "BFS cannot handle branching factor > 2.",
            "BFS requires a heuristic function h(n).",
            "BFS stores nodes in a LIFO stack."
        ],
        "answer": "BFS treats all edges as equal step cost (c=1) and optimizes for fewest edge hops, not cumulative distance g(n).",
        "hint": "BFS expands by depth d rather than cumulative edge path cost g(n).",
        "explanation": "BFS expands shallowest nodes first (fewer hops), which ignores non-uniform physical distances. UCS or A* must be used for varying step costs."
    },
    {
        "id": 40,
        "module": "Module 3",
        "topic": "Commutative Production Systems",
        "type": "Conceptual MCQ",
        "question": "In problem space theory, a Production System is defined as commutative if:",
        "options": [
            "The order of rule application to reach goal does not affect final state, and applying one rule never prevents subsequent application of another previously applicable rule.",
            "Every rule has an exact inverse rule reversing its operation.",
            "The system executes forward and backward chaining simultaneously.",
            "Working memory capacity grows linearly with depth."
        ],
        "answer": "The order of rule application to reach goal does not affect final state, and applying one rule never prevents subsequent application of another previously applicable rule.",
        "hint": "Operations commute when execution order does not alter validity or outcome.",
        "explanation": "Commutative production systems allow rule execution in any order without invalidating remaining applicable rules or blocking goal paths."
    },
    {
        "id": 41,
        "module": "Module 3",
        "topic": "Min-Conflicts CSP Local Search",
        "type": "Problem-Solving / Numerical",
        "question": "4-Queens local search: Fixed Q1(1,1), Q3(3,2), Q4(4,1). Q2 currently at (2,1). If relocating Q2 in Column 2, to which row will Q2 be moved to minimize conflicting queen pairs?",
        "options": ["Row 1", "Row 2", "Row 3", "Row 4"],
        "answer": "Row 4",
        "hint": "Evaluate attacking pairs for Q2 at rows 1, 2, 3, and 4 against fixed queens.",
        "explanation": "Row 1 (2 conflicts), Row 2 (2 conflicts), Row 3 (1 conflict), Row 4 (0 conflicts). Row 4 yields 0 conflicts."
    },
    {
        "id": 42,
        "module": "Module 3",
        "topic": "Tree Search vs. Graph Search Memory",
        "type": "Assertion-Reason",
        "question": "Assertion (A): In state spaces with cycles, Graph Search guarantees avoiding infinite loops, whereas Tree Search can loop infinitely.\nReason (R): Graph Search maintains an explored set of visited states, trading linear space O(b*m) for exponential space O(b^d).",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "answer": "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
        "hint": "Consider why storing expanded states in a closed list prevents cyclic loops at the expense of memory.",
        "explanation": "Graph Search stores all expanded nodes in an explored set to detect cycles, eliminating infinite loops but increasing space to O(b^d)."
    },
    {
        "id": 43,
        "module": "Module 3",
        "topic": "Stochastic Environments & AND-OR Trees",
        "type": "Scenario / Application",
        "question": "Robotic cleanroom arm gripping wafer: 80% success, 20% slip. What structural search tree model must the agent construct for planning under such non-deterministic outcomes?",
        "options": [
            "AND-OR Search Tree",
            "Minimax Search Tree",
            "Constraint Propagation Tree",
            "Depth-First Spanning Tree"
        ],
        "answer": "AND-OR Search Tree",
        "hint": "Agent choices form OR nodes; environment contingent outcomes form AND nodes.",
        "explanation": "AND-OR trees model contingent non-deterministic choices: OR nodes represent agent actions; AND nodes represent environment outcomes."
    },
    {
        "id": 44,
        "module": "Module 3",
        "topic": "Problem Formulation Components",
        "type": "Match the Following",
        "question": "Match 8-puzzle formulation elements:\n1. State Space -> Q. 181,440 reachable 3x3 arrangements\n2. Initial State -> S. Specific starting tile configuration\n3. Action Model -> P. Set of moves {Up, Down, Left, Right}\n4. Path Cost -> R. Each move costs 1 unit",
        "options": [
            "1-Q, 2-S, 3-P, 4-R",
            "1-P, 2-Q, 3-R, 4-S",
            "1-Q, 2-P, 3-S, 4-R",
            "1-S, 2-R, 3-Q, 4-P"
        ],
        "answer": "1-Q, 2-S, 3-P, 4-R",
        "hint": "Distinguish global set of configurations from starting setup and move operators.",
        "explanation": "State Space = reachable configurations; Initial State = start setup; Action Model = move operators; Path Cost = step unit sum."
    },
    {
        "id": 45,
        "module": "Module 3",
        "topic": "Memory-Bounded Heuristic Search",
        "type": "Fill in the Blanks",
        "question": "_____ applies iterative deepening using f-cost limit thresholds, whereas _____ drops the node with the worst f-value when memory is full, storing backup values in parent nodes.",
        "options": [
            "IDA* (Iterative Deepening A*) / SMA* (Simplified Memory-Bounded A*)",
            "SMA* / IDA*",
            "Greedy Best-First Search / Recursive Best-First Search (RBFS)",
            "Hill Climbing / Simulated Annealing"
        ],
        "answer": "IDA* (Iterative Deepening A*) / SMA* (Simplified Memory-Bounded A*)",
        "hint": "One algorithm cuts off search at f-cost limits; the other prunes memory buffer leaves.",
        "explanation": "IDA* uses f-cost limit thresholds per iteration. SMA* retains a fixed memory buffer and prunes highest f-value nodes when full."
    },
    {
        "id": 46,
        "module": "Module 3",
        "topic": "Learning Agent Architecture",
        "type": "Scenario / Application",
        "question": "In the 4-component learning agent (Performance Element, Critic, Learning Element, Problem Generator), which component proposes exploratory actions that yield new long-term knowledge?",
        "options": [
            "Performance Element",
            "Critic",
            "Learning Element",
            "Problem Generator"
        ],
        "answer": "Problem Generator",
        "hint": "Responsible for proposing novel exploratory actions to avoid habitual sub-optimal behavior.",
        "explanation": "The Problem Generator suggests exploratory actions that discover new state space features, balancing exploration vs exploitation."
    },
    {
        "id": 47,
        "module": "Module 3",
        "topic": "Admissibility of Grid Heuristics",
        "type": "Problem-Solving / Numerical",
        "question": "8-connected grid with uniform step cost c=1. Heuristics: hManhattan = Δx + Δy, hChebyshev = max(Δx, Δy). Which heuristic is admissible for A* search?",
        "options": [
            "Only hManhattan is admissible.",
            "Only hChebyshev is admissible.",
            "Both are admissible.",
            "Neither is admissible."
        ],
        "answer": "Only hChebyshev is admissible.",
        "hint": "Check if moving diagonally allows reaching a goal in fewer steps than Δx + Δy.",
        "explanation": "Diagonal moves reduce both Δx and Δy simultaneously at cost 1, so minimal true cost h* = max(Δx, Δy) = hChebyshev. hManhattan overestimates diagonal moves."
    },
    {
        "id": 48,
        "module": "Module 3",
        "topic": "CSP Value-Ordering Heuristics",
        "type": "MCQ",
        "question": "While MRV (fail-first principle) selects variables in CSP backtracking, which heuristic orders values to maximize finding a solution without backtracking?",
        "options": [
            "Least Constraining Value (LCV) Heuristic",
            "Degree Heuristic",
            "Most Constraining Value Heuristic",
            "Max-Conflicts Value Ordering"
        ],
        "answer": "Least Constraining Value (LCV) Heuristic",
        "hint": "Choose the value that leaves the maximum flexibility for neighbor variables.",
        "explanation": "Least Constraining Value (LCV) chooses the value that rules out the fewest choices for unassigned neighbor variables, maximizing success."
    },
    {
        "id": 49,
        "module": "Module 3",
        "topic": "Production Rules & Forward vs. Backward Chaining",
        "type": "True/False",
        "question": "True or False: Backward Chaining is a data-driven process starting from facts in working memory and continuously firing rules until no further rules can fire.",
        "options": ["True", "False"],
        "answer": "False",
        "hint": "Is Backward Chaining data-driven (from facts) or goal-driven (from hypothesis)?",
        "explanation": "False. Forward Chaining is data-driven (from facts). Backward Chaining is goal-driven (starting from a hypothesis and working backward)."
    },
    {
        "id": 50,
        "module": "Module 3",
        "topic": "Principle of Maximum Expected Utility",
        "type": "Conceptual MCQ",
        "question": "Under decision theory and uncertainty, an agent is defined as rational if and only if it selects actions that maximize its:",
        "options": [
            "Actual performance measure in all outcomes regardless of probability.",
            "Expected Utility (MEU), calculated as the sum of utilities of all possible outcomes weighted by their probabilities.",
            "Worst-case performance bound (Minimax payoff).",
            "Heuristic evaluation function h(n)."
        ],
        "answer": "Expected Utility (MEU), calculated as the sum of utilities of all possible outcomes weighted by their probabilities.",
        "hint": "Rationality under uncertainty balances outcome utility U(s') with transition probability P(s'|a,e).",
        "explanation": "Maximum Expected Utility (MEU) states a rational agent chooses action 'a' maximizing ∑ P(s'|a,e) * U(s')."
    }
]