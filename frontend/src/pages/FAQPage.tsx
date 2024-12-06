// frontend/src/pages/FAQPage.tsx
import React from "react";
import FAQList from "../components/FAQ/FAQList";
import { Card } from "../components/ui/card";

const FAQPage = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <Card className="bg-white shadow-lg rounded-lg p-6">
        <h1 className="text-3xl font-bold mb-6">Common Questions</h1>
        <FAQList />
      </Card>
    </div>
  );
};

export default FAQPage;
