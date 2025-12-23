// VANTAGE MVP — FRONTEND SCAFFOLD
// Stack: Next.js (App Router) + Tailwind + Framer Motion
// This is an MVP platform prototype, NOT a landing page

'use client'

import { motion } from 'framer-motion'

const bounties = [
  {
    id: 1,
    title: 'Clean & Normalize Census Dataset',
    domain: 'STEM',
    hours: '6–8 hrs',
    reward: '$180',
    skills: ['Python', 'pandas', 'data validation'],
    company: 'Local Non-Profit (Verified)'
  },
  {
    id: 2,
    title: 'SEO Architecture Audit',
    domain: 'Growth',
    hours: '4–6 hrs',
    reward: '$150',
    skills: ['SEO', 'Site Mapping', 'Analytics'],
    company: 'Early-Stage Startup'
  },
  {
    id: 3,
    title: 'Competitor Intelligence Report',
    domain: 'Business Intelligence',
    hours: '8–10 hrs',
    reward: '$220',
    skills: ['Market Research', 'Excel', 'Strategic Analysis'],
    company: 'SMB Retail Brand'
  }
]

export default function VantageDashboard() {
  return (
    <div className="min-h-screen bg-[#0A0A0F] text-white px-10 py-8">
      {/* HEADER */}
      <header className="flex justify-between items-center mb-10">
        <h1 className="text-2xl font-semibold tracking-wide">VANTAGE</h1>
        <span className="text-sm opacity-60">Neural Meritocracy Interface</span>
      </header>

      {/* BOUNTY TERMINAL */}
      <section>
        <h2 className="text-lg mb-4 opacity-80">Available Micro-Bounties</h2>

        <div className="grid grid-cols-1 gap-4">
          {bounties.map((bounty) => (
            <motion.div
              key={bounty.id}
              whileHover={{ scale: 1.01 }}
              className="rounded-xl bg-white/5 backdrop-blur-md border border-white/10 p-6"
            >
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-xl font-medium">{bounty.title}</h3>
                  <p className="text-sm opacity-60 mt-1">{bounty.company}</p>
                </div>
                <span className="text-sm px-3 py-1 rounded-full bg-white/10">
                  {bounty.domain}
                </span>
              </div>

              <div className="mt-4 flex flex-wrap gap-2">
                {bounty.skills.map((skill) => (
                  <span
                    key={skill}
                    className="text-xs px-2 py-1 rounded bg-white/10"
                  >
                    {skill}
                  </span>
                ))}
              </div>

              <div className="mt-5 flex justify-between text-sm opacity-80">
                <span>{bounty.hours}</span>
                <span>{bounty.reward}</span>
              </div>
            </motion.div>
          ))}
        </div>
      </section>
    </div>
  )
}
