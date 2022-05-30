# Intro

Usually, lectures, articles and videos about quantum computation mostly talk about qubits themselves, and all the quantum phenomena that make qubits exciting, futuristic, and almost impossible to fully understand.

Qubits on their own, however, don't form a working quantum computer. The qubit might be the most spectacular element of the computer, but many more layers are needed to actually work with the quantum phenomena that give the quantum computer its great powers.

This Professional Certificate will touch on all of these layers: from the devices which bridge the gap between the quantum chip and the classical control hardware, to the mathematical aspects of some quantum algorithms. The program is divided into two parts: this MOOC, the first part, will talk about the materials, four different qubits and operations on these qubits. The second MOOC, "Architecture, Algorithms, and Protocols of a Quantum Computer and Quantum Internet", will start on 31 January 2020 and will run alongside this course until 31 July 2020. By completing both parts, you will have a complete overview of all building blocks of a quantum computer!

In this course, you will learn:

How all the building blocks of a quantum computer work, and deeper information on the qubits which lie at the heart of a quantum computer and internet. How qubits can be used and controlled efficiently, and the workings of the four most promising types of solid-state qubits: Silicon Spin Qubit, Diamond NV Center Qubit, Superconducting Transmon Qubit and Topological Qubit. Get the most out of this course! This course aims to give you an understanding of the scientific basis behind the quantum computer and a quantum internet; and of four different qubits. Our challenge to you is to really understand the working principles of qubits and, at the same time, the working principles of a computer made of these qubits.

This course is about getting an insight in the four different types of qubits, the essential element at the heart of a quantum computer and a quantum internet. We will inspire each other and we ask that you bring in your experiences, your insights and your thoughts via the forums. So the key message is: don't be afraid to share.

Course structure and syllabus

This course runs from 4 September 2018 until 31 May 2019. The course materials are still available to you after this date, but you will not be able to complete quizzes and graded elements after the course closes.

The course materials are grouped into 6 modules. All modules are available to you right away.

If you have enrolled for a verified Certificate of Achievement you can generate your own certificate at any time after you have qualified to pass the course. To qualify for a certificate, you must achieve a total grade of 60% or higher. You can check your grade at any time under the course’s Progress page. You can find that link at the top of every page if you view the course from a desktop computer.

An ID verified Certificate of Achievement is available. You can upgrade on your edX Dashboard to Verified during the course. This course talks about the building blocks of a quantum computer. We start off with introducing the first layer, the qubit, in more detail. In the MOOC Building Blocks of a Quantum Computer - part 2, we continue this course by explaining the other essential layers that make a quantum computer.

An overview of the course's 6 modules:

Module 1. Introducing the building blocks of a quantum computer

Lecture 1 + Quiz: Introduction of the building blocks of a quantum computer - Koen Bertels

Lecture 2 + Quiz: Quantum materials - Giordano Scappuci

Lecture 3 + Quiz: Ket notation - Ben Criger

Module 2. The Spin Qubit

Lecture 4 + Quiz: The spin qubit - Lieven Vandersypen

Lecture 5 + Quiz: Operations on spin qubits - Menno Veldhorst

Module 3. The NV Center Qubit

Lecture 6 + Quiz: The NV center qubit - Tim Timiniau

Lecture 7 + Quiz: Operations on NV center qubits - Tim Timiniau

Module 4.

The Superconducting Qubit Lecture 8 (3 videos) + Quiz: The superconducting qubit - Leo DiCarlo Lecture 9 (3 videos) + Quiz: Operations on superconducting qubits - Brian Tarasinski, Adriaan Rol, Niels Bultink

Module 5. The Topological Qubit

Lecture 10 + Quiz: The topological qubit - Michael Wimmer Lecture 11 + Quiz: Operations on topological qubits - Attila Geresdi

Module 6. Wrap up & preview 'Building Blocks Part 2'

Lecture 12 + Final Exam (25%): wrap up and preview - Menno Veldhorst

The syllabus will provide you with more information on these 3 topics:

A. Module-by-module overview of the course B. Grading and assessment C. Discussion Forum Guidelines

You may always access the syllabus in the top menu of this webpage. Feel free to jump there now, and continue here later on.

# Part I Access the Quantum Library

The Quantum Library is a separate module in the course where you can find videos explaining various quantum principles. When watching a lecture, you can always refer back to this library to gain a better understanding. The module will always be the last one in the course, and is also linked at the top of each page, if you are viewing on a tablet/desktop.

Researcher at QuTech The Quantum Library is a separate module in the course where you can find videos explaining various quantum principles. When watching a lecture, you can always refer back to this library to gain a better understanding. The module will always be the last one in the course, and is also linked at the top of each page, if you are viewing on a tablet/desktop.

The Quantum Library is a separate module in the course where you can find videos explaining various quantum principles. When watching a lecture, you can always refer back to this library to gain a better understanding. The module will always be the last one in the course, and is also linked at the top of each page, if you are viewing on a tablet/desktop

Q Library pointed out

These topics appear in the Quantum Library:

entanglement - different ways of entanglement - teleportation - measurement - measurement in superposition - repeaters

Each topic contains a short video, and is followed by an ungraded quiz to test your knowledge.Please check out the topics (and test your knowledge!) in the Quantum Library.

## Entanglement

Quantum entanglement is a special connection between two qubits. There are many ways to generate entanglement. One way to produce it is by bringing two qubits close together, perform an operation to entangle them and then move them apart again. When they are entangled, you can move them arbitrarily far apart from each other and they will remain entangled. This entanglement will manifest itself in the outcomes of measurements on these qubits. When measured these qubits will always yield zero or one perfectly at random, but no matter how far away they are from each other, they will always yield the same outcome.

Entanglement has two very special properties that enable all the applications derived from it.

1. The first property is that entanglement cannot be shared. If two qubits are maximally entangled with each other, then no other party in the universe can have a share of this entanglement. This property is called the monogamy of entanglement.

2. The second property of entanglement, which makes it so powerful, is called maximal coordination. This property manifests itself when measuring the qubits.

When two qubits that are entangled are measured in the same basis, no matter how far away they are from each other, they will always yield the same outcome. This outcome is not decided beforehand, but it is completely random and is decided when the measurement happens.

It’s almost romantic to think that two particles can be entangled even when they are millions of kilometres apart. Learn more about quantum entanglement. How is it generated and what are the implications?

Entanglement further explained

### Entanglement further explained

So now I’d like to explain to you the phenomenon of entanglement. So what is entanglement precisely? Imagine we have 2 particles: we have particle A and particle B. And these particles can be either full, which is the filled have here, empty, or a superposition of the two. Now let’s say that particle A and B are entangled. The weird thing about this entanglement is that when we would measure one of the particles, say we’d like to measure particle A, and we get the outcome/result full. Instantaneously the particle at B collapses into the full state as well. This happens instantaneously, so even faster than the speed of light.

However, particle B, or an observer at particle B would never know if Alice, the observer at A has already measured her particle. In order for him to know if Alice measured her particle, Alice needs to send a signal over a classical internet, which cannot exceed the speed of light, to notify Bob, who is at particle B, if the particle has been measured. Only then they can compare their results and see if their particles were indeed entangled. The particles can also be entangled in a different way. So, this corresponds to when the particle A would be full when we measure it, particle B would be empty, and vice versa: if A would result in empty, B would result in full. If we do not know beforehand which kind of entanglement we have, we can also not know what the state of B will be after measuring A.

Question 1: Entanglement from relative phases

In Module 1, we note that entangled states are those that cannot be written as tensor products.

The tensor product of two single-qubit states looks like this:

$\left[\begin{array}{c}
\alpha\\
\beta
\end{array}\right]\otimes\left[\begin{array}{c}
\gamma\\
\delta
\end{array}\right]=\left[\begin{array}{c}
\alpha\gamma\\
\alpha\delta\\
\beta\gamma\\
\beta\delta
\end{array}\right]$