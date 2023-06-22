'use client'
import { ThemeProvider } from '@mui/material/styles'
import './globals.css'
import { baseTheme } from './assets/global/Theme-variable'

import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })


export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const theme = baseTheme;

  return (
    <ThemeProvider theme={theme}> 
      <html lang="en">
        <body className={inter.className}>{children}</body>
      </html>
    </ThemeProvider>

  )
}
