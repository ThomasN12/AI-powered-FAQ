// frontend/src/mocks/faqData.ts
export const mockFAQs = [
  {
    id: 1,
    question: "What's the best way to learn Python programming?",
    answer:
      "Start with Python basics like variables, data types, and control structures. Practice with small projects, use resources like freeCodeCamp or Codecademy, and join Python communities on Reddit. Focus on understanding concepts before moving to complex topics.",
    related_questions: [
      "How long does it take to learn Python?",
      "Is Python good for beginners?",
      "What projects should I start with in Python?",
    ],
  },
  {
    id: 2,
    question: "How do I set up a development environment for React?",
    answer:
      "Use Create React App for a quick start: Run 'npx create-react-app my-app'. Install Node.js first if you haven't. VS Code is recommended as an editor. For more control, consider configuring Webpack and Babel manually.",
    related_questions: [
      "What IDE is best for React?",
      "Should I use TypeScript with React?",
      "Create React App vs Manual Setup?",
    ],
  },
  {
    id: 3,
    question: "What are the key concepts of Git version control?",
    answer:
      "Git's core concepts include repositories, commits, branches, and merging. Start by understanding basic commands like git add, commit, push, and pull. Learn branching strategies and how to resolve merge conflicts.",
    related_questions: [
      "How to undo changes in Git?",
      "What's the difference between git fetch and pull?",
      "How to handle merge conflicts?",
    ],
  },
];
