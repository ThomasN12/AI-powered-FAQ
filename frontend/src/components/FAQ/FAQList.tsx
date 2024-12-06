// frontend/src/components/FAQ/FAQList.tsx
import React, { useEffect, useState } from "react";
import {
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Typography,
} from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
// import { mockFAQs } from "../../mocks/faqData";

interface FAQ {
  id: number;
  question: string;
  question_body: string;
  answer: string;
  related_questions: string[];
}

const FAQList = () => {
  const [faqs, setFaqs] = useState<FAQ[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/api/faq")
      .then((res) => res.json())
      .then((data) => {
        setFaqs(data);
        setLoading(false);
      });
  }, []);

  // Replace fetch with:
  // useEffect(() => {
  //   setFaqs(mockFAQs);
  //   setLoading(false);
  // }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {faqs.map((faq, index) => (
        <Accordion key={index} className="mb-4">
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6" className="font-bold">
              {faq.question}
            </Typography>
          </AccordionSummary>
          <AccordionDetails>
            {/* Question content */}
            {faq.question_body && (
              <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                <Typography className="text-gray-700">
                  {faq.question_body}
                </Typography>
              </div>
            )}

            {/* Answer section */}
            <div className="border-l-4 border-blue-500 pl-4">
              <Typography className="font-semibold mb-2 text-blue-700">
                Best Answer:
              </Typography>
              <Typography className="text-gray-800">{faq.answer}</Typography>
            </div>

            {/* Related Questions */}
            {faq.related_questions.length > 0 && (
              <div className="mt-6 pt-4 border-t border-gray-200">
                <Typography
                  variant="subtitle2"
                  className="font-semibold text-gray-600"
                >
                  Related Questions:
                </Typography>
                <ul className="mt-2 list-disc pl-5">
                  {faq.related_questions.map((q, i) => (
                    <li key={i}>
                      <Typography className="text-gray-600">{q}</Typography>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </AccordionDetails>
        </Accordion>
      ))}
    </div>
  );
};

export default FAQList;
